from django.shortcuts import render, redirect
from django.views import View
from guide.forms import SurfSpotForm, DangerForm

# Create your views here.
from guide.models import SurfSpot


class HomeView(View):

    def get(self, request):
        return render(request, 'home.html')


class SpotListView(View):

    def get(self, request):
        spots = SurfSpot.objects.all()
        return render(request, 'spot_list.html', {'spots': spots})


class SpotView(View):

    def get(self, request, pk):
        spot = SurfSpot.objects.get(id=pk)
        return render(request, 'spot.html', {'spot': spot})


class AddSpotView(View):

    def get(self, request):
        form = SurfSpotForm()
        return render(request, 'add_spot.html', {'form': form})

    def post(self, request):
        form = SurfSpotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('spot-list')
        return redirect('spot-list')
