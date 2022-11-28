from django.shortcuts import render, redirect
from django.views import View
from guide.forms import SurfSpotForm, DangerForm

# Create your views here.
from guide.models import SurfSpot


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
