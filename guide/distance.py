import folium
from geopy.geocoders import Nominatim


def get_map(location):
    # getting a latitude and longitude of localisation
    geocoder = Nominatim(user_agent='eliasz')

    coordinates = geocoder.geocode(location)

    # creating longitude and latitude
    lat_long = [coordinates.latitude, coordinates.longitude]


    # variables of coordinates of locations
    place1 = (lat_long[0], lat_long[1])

    # creating map object with folium plot
    map = folium.Map()

    # creating points on map
    folium.Marker(place1).add_to(map)

    if f'map{location}.html' not in '/Users/eliasz/Desktop/SurferGuide/guide/static/maps/':
        map.save(f'/Users/eliasz/Desktop/SurferGuide/guide/static/maps/{location}.html')

get_map('Chałupy')

