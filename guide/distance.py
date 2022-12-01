import folium
from geopy.geocoders import Nominatim


def get_map(location):
    geocoder = Nominatim(user_agent='eliasz')

    coordinates = geocoder.geocode(location)

    latitude = coordinates.latitude
    longitude = coordinates.longitude

    place = (latitude, longitude)

    map = folium.Map(width=1248, height=500, location=place, zoom_start=10, max_height=500, max_width=1214)

    # creating points on map
    folium.Marker(place).add_to(map)
    map = map._repr_html_()

    return map


def get_map_many_locations(locations):
    geocoder = Nominatim(user_agent='eliasz')

    map = folium.Map(width=1214, height=500, zoom_start=10, max_height=500, max_width=1214)

    # creating points on map
    for location in locations:
        coordinates = geocoder.geocode(location)
        latitude = coordinates.latitude
        longitude = coordinates.longitude
        place = (latitude, longitude)
        folium.Marker(place).add_to(map)
    map = map._repr_html_()

    return map


