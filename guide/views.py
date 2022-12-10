from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from guide.forms import SurfSpotForm, RegisterForm, LoginForm, AddPhotoForm, CommentAddForm, ProfileSettingsForm
from guide.models import SurfSpot, Photo, UserInformation, Comment
from guide.maps import get_map, get_map_many_locations
from guide.filters import SurfSpotFilter


# Create your views here.


class HomeView(View):

    def get(self, request):
        last_added_spots = SurfSpot.objects.all().order_by('-id')[:3]
        last_added_photos = Photo.objects.all().order_by('-id')[:4]
        logged_user = request.user
        spots = SurfSpot.objects.all()
        locations = []
        for spot in spots:
            locations.append(spot.location)
        map = get_map_many_locations(locations)

        context = {
            'last_added_spots': last_added_spots,
            'last_added_photos': last_added_photos,
            'logged_user': logged_user,
            'map': map,

        }
        return render(request, 'home.html', context)


class SpotListView(View):

    def get(self, request):
        europe = SurfSpot.objects.filter(continent='EU')
        asia = SurfSpot.objects.filter(continent='AS')
        africa = SurfSpot.objects.filter(continent='AF')
        north_america = SurfSpot.objects.filter(continent='NA')
        south_america = SurfSpot.objects.filter(continent='SA')
        oceania = SurfSpot.objects.filter(continent='OC')
        logged_user = request.user

        context = {
            'europe': europe,
            'asia': asia,
            'africa': africa,
            'north_america': north_america,
            'south_america': south_america,
            'oceania': oceania,
            'logged_user': logged_user,
        }
        return render(request, 'spot_list.html', context)


class SpotEditView(PermissionRequiredMixin, UpdateView):
    permission_required = 'guide.change_surfspot'

    model = SurfSpot
    form_class = SurfSpotForm
    template_name = 'spot_edit.html'

    def get_success_url(self):
        return f'/spot/{self.kwargs["pk"]}/'


class DeleteSpotView(PermissionRequiredMixin, DeleteView):
    permission_required = 'guide.delete_surfspot'

    model = SurfSpot
    template_name = 'delete_spot.html'
    success_url = '/spot-list'

    def post(self, request, pk):
        spot = SurfSpot.objects.get(id=pk)
        spot.delete()
        return redirect('/spot-list')


class SpotView(View):

    def get(self, request, pk):
        spot = SurfSpot.objects.get(id=pk)
        best_seasons = spot.best_season.all()
        photos = Photo.objects.filter(surfspot=spot)
        comments = Comment.objects.filter(surfspot=spot)
        form = CommentAddForm()
        photo_form = AddPhotoForm()
        map = get_map(spot.location)
        context = {

            'spot': spot,
            'best_seasons': best_seasons,
            'photos': photos,
            'comments': comments,
            'form': form,
            'photo_form': photo_form,
            'map': map,
        }
        return render(request, 'spot.html', context)


class AddSpotView(LoginRequiredMixin, View):

    def get(self, request):
        logged_user = request.user
        form = SurfSpotForm()
        return render(request, 'add_spot.html', {'form': form, 'logged_user': logged_user})

    def post(self, request):
        form = SurfSpotForm(request.POST)
        if form.is_valid():
            spot = form.save()
            return redirect('spot', pk=spot.pk)
        return render(request, 'add_spot.html', {'form': form})


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        register = 'Don\'t have an account? Register here!'
        return render(request, 'login.html', {'form': form, 'register': register})

    def post(self, request):
        form = LoginForm(request.POST)
        message = ''
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            message = 'Invalid username or password!'
        return render(request, 'login.html', {'form': form, 'message': message})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create(username=username, password=password)
            user.set_password(password)
            info = UserInformation.objects.create(user=user)
            user.save()
            info.save()
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, 'login.html', {'form': form})


class AddPhotoView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['image']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.surfspot = SurfSpot.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return f'/spot/{self.kwargs["pk"]}/'

    def get_template_names(self):
        return f'/spot/{self.kwargs["pk"]}/'


class ProfileView(View):

    def get(self, request, pk):
        profile_user = User.objects.get(id=pk)
        info = UserInformation.objects.get(user=profile_user)
        photos = Photo.objects.filter(user=profile_user).order_by('-id')[:4]
        visited_spots = UserInformation.objects.get(user=profile_user).visited_spots.all()
        visited_locations = []
        map = None
        for spot in visited_spots:
            visited_locations.append(spot.location)
        if info.home_spot:
            visited_locations.append(info.home_spot.location)
        if len(visited_locations) == 1:
            map = get_map(visited_locations[0])
        elif len(visited_locations) > 1:
            map = get_map_many_locations(visited_locations)
        context = {
            'photos': photos,
            'info': info,
            'visited_spots': visited_spots,
            'map': map,
            'profile_user': profile_user,

        }
        return render(request, f'profile.html', context)


class ProfileSettingsView(LoginRequiredMixin, UpdateView):
    model = UserInformation
    user = User
    template_name = 'profile_settings.html'
    form_class = ProfileSettingsForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return f'/profile/{self.request.user.id}/'

    def get_object(self, queryset=None):
        user_id = self.request.user.id
        return UserInformation.objects.get(user_id=user_id)


class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.surfspot = SurfSpot.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return f'/spot/{self.kwargs["pk"]}/'

    def get_template_names(self):
        return f'/spot/{self.kwargs["pk"]}/'


class TripPlannerView(LoginRequiredMixin, View):

    def get(self, request):
        spots = SurfSpot.objects.all()
        spots_filter = SurfSpotFilter(request.GET, queryset=spots)
        return render(request, 'trip_planner.html', {'filter': spots_filter})
