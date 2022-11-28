from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from guide.forms import SurfSpotForm, DangerForm


# Create your views here.
from guide.models import SurfSpot


class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request):
        return render(request, self.template_name)


class SpotListView(TemplateView):

    def get(self, request):
        spots = SurfSpot.objects.all()
        return render(request, 'spot_list.html', {'spots': spots})

class SpotView(TemplateView):
    template_name = 'spot.html'

    def get(self, request):
        return render(request, self.template_name)


class AddSpotView(TemplateView):

    def get(self, request):
        form = SurfSpotForm()
        return render(request, 'add_spot.html', {'form': form})

    def post(self, request):
        form = SurfSpotForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('spot-list')
        return redirect('spot-list')