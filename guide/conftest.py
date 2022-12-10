import pytest
from django.contrib.auth.models import User, Permission
from guide.models import Photo, SurfSpot, Comment, UserInformation, Danger, Season


@pytest.fixture
def normal_user():
    u = User.objects.create_user('test', '1234')
    return u


@pytest.fixture
def admin_user():
    u = User.objects.create_superuser('admin', '1234')
    return u


@pytest.fixture
def dangers():
    lst = []
    for n in range(10):
        d = Danger.objects.create(name=f'test{n}', description=f'test{n}')
        lst.append(d)
    return lst


@pytest.fixture
def seasons():
    lst = []
    for n in range(10):
        s = Season.objects.create(name=f'test{n}')
        lst.append(s)
    return lst


@pytest.fixture
def surf_spots():
    lst = []
    danger = Danger.objects.create(name=f'test', description='test')
    season = Season.objects.create(name=f'test')
    for n in range(3):
        s = SurfSpot.objects.create(
            name=f'test{n}',
            description='test',
            location='Warsaw',
            continent='EU',
            best_wind='N',
            wave_direction='B',
            spot_type='B',
            wave_type='G',
            swell_size=1,
            crowd=1,
            temperature_in_spring=n,
            temperature_in_summer=n,
            temperature_in_fall=n,
            temperature_in_winter=n,
        )
        s.danger.add(danger)
        s.best_season.add(season)
        lst.append(s)
    return lst


@pytest.fixture
def photos(surf_spots, normal_user):
    lst = []
    for n in range(10):
        p = Photo.objects.create(
            surfspot=surf_spots[1],
            user=normal_user,
            image='image.jpg',
        )
        lst.append(p)
    return lst


@pytest.fixture
def comments(surf_spots, normal_user):
    lst = []
    for n in range(10):
        c = Comment.objects.create(
            surfspot=surf_spots[1],
            user=normal_user,
            text=n,
        )
        lst.append(c)
    return lst


@pytest.fixture
def profile_settings(normal_user, surf_spots):
    u = UserInformation.objects.create(
        user=normal_user,
        country='test',
        continent='EU',
        bio='test',
    )
    return u
