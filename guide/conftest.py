import pytest
from django.contrib.auth.models import User, Permission
from guide.models import Photo, SurfSpot, Comment, UserInformation, Danger, Season


@pytest.fixture
def user_without_permission():
    u = User.objects.create_user('test', '1234')
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
def surfspots():
    lst = []
    danger = Danger.objects.create(name=f'test', description='test')
    season = Season.objects.create(name=f'test')
    for n in range(10):
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
def photos(surfspots, user_without_permission):
    lst = []
    for n in range(10):
        p = Photo.objects.create(
            surfspot=surfspots[1],
            user=user_without_permission,
            image='image.jpg',
        )
        lst.append(p)
    return lst


@pytest.fixture
def comments(surfspots, user_without_permission):
    lst = []
    for n in range(10):
        c = Comment.objects.create(
            surfspot=surfspots[1],
            user=user_without_permission,
            text=n,
        )
        lst.append(c)
    return lst


@pytest.fixture
def userinformation(user_without_permission, surfspots):
    n = 1
    u = UserInformation.objects.create(
        user=user_without_permission,
        country=n,
        continent=n,
        bio=n,
        home_spot=surfspots[n],
        board=n,
        skill_level=1,
        achievements=n,
        visited_spots=surfspots[n],
    )
    return u
