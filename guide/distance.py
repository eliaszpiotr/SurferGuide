import folium
from geopy.geocoders import Nominatim

def get_map(location):
    geocoder = Nominatim(user_agent='eliasz')

    coordinates = geocoder.geocode(location)

    latitude = coordinates.latitude
    longitude = coordinates.longitude

    place = (latitude, longitude)

    map = folium.Map(width=1214, height=500, location=place, zoom_start=10, max_height=500, max_width=1214)

    # creating points on map
    folium.Marker(place).add_to(map)
    map = map._repr_html_()

    return map

