from django.test import Client
from guide.conftest import *
from guide.models import *
from guide.forms import *


# home view tests
@pytest.mark.django_db
def test_home_view():
    client = Client()
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_home_view_context(surf_spots, photos, normal_user):
    client = Client()
    url = reverse('home')
    response = client.get(url)
    client.force_login(normal_user)
    assert response.status_code == 200
    assert 'last_added_spots' in response.context
    assert 'last_added_photos' in response.context
    assert 'logged_user' in response.context
    assert 'map' in response.context
    assert len(response.context['last_added_spots']) == 3
    assert len(response.context['last_added_photos']) == 4
    assert response.context['map'] is not None


# spot list view tests
@pytest.mark.django_db
def test_spot_list_view():
    client = Client()
    url = reverse('spot-list')
    response = client.get(url)
    assert response.status_code == 200



@pytest.mark.django_db
def test_spot_list_view_context(surf_spots, normal_user):
    client = Client()
    url = reverse('spot-list')
    response = client.get(url)
    client.force_login(normal_user)
    assert response.status_code == 200
    assert 'europe' in response.context
    assert 'asia' in response.context
    assert 'africa' in response.context
    assert 'north_america' in response.context
    assert 'south_america' in response.context
    assert 'oceania' in response.context
    assert 'logged_user' in response.context
    assert len(response.context['europe']) == 3
    assert len(response.context['asia']) == 0
    assert len(response.context['africa']) == 0
    assert len(response.context['north_america']) == 0
    assert len(response.context['south_america']) == 0
    assert len(response.context['oceania']) == 0
    assert response.context['logged_user'] is not None


@pytest.mark.django_db
def test_spot_list_content(surf_spots, normal_user):
    client = Client()
    url = reverse('spot-list')
    response = client.get(url)
    client.force_login(normal_user)
    assert response.status_code == 200
    assert b'Europe' in response.content
    assert b'Asia' not in response.content
    assert b'Africa' not in response.content
    assert b'North America' not in response.content
    assert b'South America' not in response.content
    assert b'Oceania' not in response.content
    assert b'Login' in response.content


# edit spot view tests
@pytest.mark.django_db
def test_spot_edit_view(surf_spots, admin_user):
    client = Client()
    client.force_login(admin_user)
    url = reverse('spot-edit', kwargs={'pk': surf_spots[0].pk})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_spot_edit_view_not_logged(surf_spots):
    client = Client()
    url = reverse('spot-edit', kwargs={'pk': surf_spots[0].pk})
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_spot_edit_view_not_admin(surf_spots, normal_user):
    client = Client()
    client.force_login(normal_user)
    url = reverse('spot-edit', kwargs={'pk': surf_spots[0].pk})
    response = client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_spot_edit_form(surf_spots, admin_user):
    client = Client()
    client.force_login(admin_user)
    url = reverse('spot-edit', kwargs={'pk': surf_spots[0].pk})
    response = client.get(url)
    form = response.context['form']
    assert isinstance(form, SurfSpotForm)
    assert form.instance == surf_spots[0]


# delete spot view tests
@pytest.mark.django_db
def test_delete_spot_view(surf_spots, admin_user):
    client = Client()
    client.force_login(admin_user)
    url = reverse('delete', kwargs={'pk': surf_spots[0].pk})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_spot_view_not_logged(surf_spots):
    client = Client()
    url = reverse('delete', kwargs={'pk': surf_spots[0].pk})
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_delete_spot_view_not_admin(surf_spots, normal_user):
    client = Client()
    client.force_login(normal_user)
    url = reverse('delete', kwargs={'pk': surf_spots[0].pk})
    response = client.get(url)
    assert response.status_code == 403


# spot detail view tests
@pytest.mark.django_db
def test_spot_view(surf_spots):
    client = Client()
    url = reverse('spot', kwargs={'pk': surf_spots[0].pk})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_spot_view_context(surf_spots, photos, normal_user):
    client = Client()
    url = reverse('spot', kwargs={'pk': surf_spots[0].pk})
    response = client.get(url)
    client.force_login(normal_user)
    assert response.status_code == 200
    assert 'spot' in response.context
    assert 'photos' in response.context
    assert 'map' in response.context
    assert response.context['spot'] == surf_spots[0]
    assert len(response.context['photos']) == 0
    assert response.context['map'] is not None


@pytest.mark.django_db
def test_spot_view_content(surf_spots, photos, normal_user):
    client = Client()
    url = reverse('spot', kwargs={'pk': surf_spots[0].pk})
    response = client.get(url)
    client.force_login(normal_user)
    assert response.status_code == 200
    assert b'Europe' in response.content
    assert b'Asia' not in response.content
    assert b'Africa' not in response.content
    assert b'North America' not in response.content
    assert b'South America' not in response.content
    assert b'Oceania' not in response.content


# add spot view tests
@pytest.mark.django_db
def test_spot_add_view(normal_user):
    client = Client()
    url = reverse('add-spot')
    client.force_login(normal_user)
    response = client.get(url)
    assert response.status_code == 200
    form = response.context['form']
    assert isinstance(form, SurfSpotForm)


@pytest.mark.django_db
def test_spot_add_view_not_logged():
    client = Client()
    url = reverse('add-spot')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_spot_add_form(surf_spots, normal_user):
    client = Client()
    client.force_login(normal_user)
    url = reverse('add-spot')
    response = client.get(url)
    form = response.context['form']
    assert isinstance(form, SurfSpotForm)


# login view tests
@pytest.mark.django_db
def test_login_view():
    client = Client()
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_view_content():
    client = Client()
    url = reverse('login')
    response = client.get(url)
    assert b'Login' in response.content
    assert b'Username' in response.content
    assert b'Password' in response.content
    assert b'Login' in response.content


@pytest.mark.django_db
def test_login_view_form():
    client = Client()
    url = reverse('login')
    response = client.get(url)
    form = response.context['form']
    assert isinstance(form, LoginForm)


@pytest.mark.django_db
def test_login_view_form_works(normal_user):
    client = Client()
    url = reverse('login')
    response = client.post(url, {'username': normal_user.username, 'password': 'password'})
    assert response.status_code == 200


# logout view tests
@pytest.mark.django_db
def test_logout_view(normal_user):
    client = Client()
    client.force_login(normal_user)
    url = reverse('logout')
    response = client.get(url)
    assert response.status_code == 302


# register view tests
@pytest.mark.django_db
def test_register_view():
    client = Client()
    url = reverse('register')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_register_view_form():
    client = Client()
    url = reverse('register')
    response = client.get(url)
    form = response.context['form']
    assert isinstance(form, RegisterForm)


@pytest.mark.django_db
def test_register_view_valid_form():
    client = Client()
    url = reverse('register')
    response = client.post(url, {'username': 'test', 'password': 'password', 'password2': 'password'})
    assert response.status_code == 302


@pytest.mark.django_db
def test_register_view_invalid_form():
    client = Client()
    url = reverse('register')
    response = client.post(url, {'username': 'test', 'password': 'password', 'password2': 'password2'})
    assert response.status_code == 200


# photo add view tests

# add comment view tests
@pytest.mark.django_db
def test_add_comment_view_not_logged(surf_spots):
    client = Client()
    url = reverse('add-comment', kwargs={'pk': surf_spots[0].pk})
    response = client.get(url)
    assert response.status_code == 302


# profile view tests
@pytest.mark.django_db
def test_profile_view(normal_user, profile_settings):
    client = Client()
    client.force_login(normal_user)
    url = reverse('profile', kwargs={'pk': normal_user.pk})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_view_not_logged(normal_user, profile_settings):
    client = Client()
    url = reverse('profile', kwargs={'pk': normal_user.pk})
    response = client.get(url)
    assert response.status_code == 200


# profile settings view tests
@pytest.mark.django_db
def test_profile_settings_view_not_logged(normal_user):
    client = Client()
    url = reverse('profile-settings', kwargs={'pk': normal_user.pk})
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_profile_settings_view_logged(normal_user, profile_settings):
    client = Client()
    client.force_login(normal_user)
    url = reverse('profile-settings', kwargs={'pk': normal_user.pk})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_profile_settings_view_form(normal_user, profile_settings):
    client = Client()
    client.force_login(normal_user)
    url = reverse('profile-settings', kwargs={'pk': normal_user.pk})
    response = client.get(url)
    form = response.context['form']
    assert isinstance(form, ProfileSettingsForm)


@pytest.mark.django_db
def test_profile_settings_view_form_works(normal_user, profile_settings):
    client = Client()
    client.force_login(normal_user)
    url = reverse('profile-settings', kwargs={'pk': normal_user.pk})
    response = client.post(url, {'bio': 'test'})
    assert response.status_code == 302


# trip planner view tests
@pytest.mark.django_db
def test_trip_planner_view(normal_user):
    client = Client()
    client.force_login(normal_user)
    url = reverse('trip-planner')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_trip_planner_view_filter(normal_user, surf_spots):
    client = Client()
    client.force_login(normal_user)
    url = reverse('trip-planner')
    response = client.get(url, {'continent': 'EU'})
    assert response.status_code == 200


@pytest.mark.django_db
def test_trip_planner_view_filter2(normal_user, surf_spots):
    client = Client()
    client.force_login(normal_user)
    url = reverse('trip-planner')
    response = client.get(url, {'continent': 'EU', 'country': 'PL'})
    assert response.status_code == 200


@pytest.mark.django_db
def test_trip_planner_view_filter_valid(normal_user, surf_spots):
    client = Client()
    client.force_login(normal_user)
    url = reverse('trip-planner')
    response = client.get(url, {'continent': 'EU', 'country': 'PL', 'city': 'Gdynia'})
    assert response.status_code == 200


# photo gallery view tests

@pytest.mark.django_db
def test_photo_gallery_view(surf_spots):
    client = Client()
    url = reverse('photo-gallery', kwargs={'pk': surf_spots[0].pk})
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_photo_gallery_context(surf_spots, photos):
    client = Client()
    url = reverse('photo-gallery', kwargs={'pk': surf_spots[0].pk})
    response = client.get(url)
    assert 'photos' in response.context








