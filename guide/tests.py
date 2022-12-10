from django.test import TestCase
import pytest
from django.urls import reverse
from django.test import Client

from .conftest import *
from .models import *
from .forms import *
from .filters import *
from django.contrib.auth.models import User


# Create your tests here.

@pytest.mark.django_db
def test_home_view():
    client = Client()
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_spot_list_view():
    client = Client()
    url = reverse('spot-list')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_spot_view(surfspots):
    client = Client()
    url = reverse('spot', kwargs={'pk': surfspots[0].pk})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_spot_add_view(user_without_permission):
    client = Client()
    url = reverse('add-spot')
    client.force_login(user_without_permission)
    response = client.get(url)
    assert response.status_code == 200
    form = response.context['form']
    assert isinstance(form, SurfSpotForm)


























