from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from guide.forms import SurfSpotForm, RegisterForm, LoginForm
from guide.models import SurfSpot


# Create your views here.


class HomeView(View):

    def get(self, request):
        last_added_spots = SurfSpot.objects.all().order_by('-id')[:3]
        return render(request, 'home.html', {'last_added_spots': last_added_spots})


class SpotListView(View):

    def get(self, request):
        europe = SurfSpot.objects.filter(continent='EU')
        asia = SurfSpot.objects.filter(continent='AS')
        africa = SurfSpot.objects.filter(continent='AF')
        north_america = SurfSpot.objects.filter(continent='NA')
        south_america = SurfSpot.objects.filter(continent='SA')
        oceania = SurfSpot.objects.filter(continent='OC')

        context = {
            'europe': europe,
            'asia': asia,
            'africa': africa,
            'north_america': north_america,
            'south_america': south_america,
            'oceania': oceania,
        }
        return render(request, 'spot_list.html', context)


class SpotView(View):

    def get(self, request, pk):
        spot = SurfSpot.objects.get(id=pk)
        return render(request, 'spot.html', {'spot': spot})


class AddSpotView(LoginRequiredMixin, View):

    def get(self, request):
        form = SurfSpotForm()
        return render(request, 'add_spot.html', {'form': form})

    def post(self, request):
        form = SurfSpotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('spot-list')
        return redirect('spot-list')


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        register = 'Don\'t have an account? Register here!'
        return render(request, 'form.html', {'form': form, 'register': register})

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
        return render(request, 'form.html', {'form': form, 'message': message})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create(username=username, password=password)
            user.set_password(password)
            user.save()
            if user is not None:
                login(request, user)
                return redirect('home')
        return render(request, 'form.html', {'form': form})

