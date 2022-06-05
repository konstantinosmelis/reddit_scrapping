import folium
import geocoder
import os
import utils
import datagenerator

def create_map():
    pos = geocoder.ip('me')
    map = folium.Map(location=pos.latlng, zoom_start=4, control_scale=True)
    map.save(os.path.abspath("templates/map.html"))
    return map


def add_markers(map, data):
    for el in data:
        if not el["location"]["latitude"] == None or not el["location"]["longitude"] == None:
            content = f"<img style='width: 300px; height: auto;' src='{el['image']}'/>"
            folium.Marker([el["location"]["latitude"], el["location"]["longitude"]], popup=content).add_to(map)
    map.save(os.path.abspath("./templates/map.html"))


def generate_map():
    map = create_map()
    data = datagenerator.get_full_data()
    add_markers(map, data)
