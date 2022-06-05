import utils
import urllib
import json
import spacy
import geocoder

def get_data():
    with urllib.request.urlopen(utils.REDDIT_URL) as response:
        json_data = json.loads(response.read().decode())
    data = []
    for post in json_data['data']['children']:
        data.append({'title': post['data']['title'], 'image': post['data']['url']})
    return data


def get_full_data():
    data = get_data()
    nlp = spacy.load("en_core_web_md")
    locations = []
    for el in data:
        doc = nlp(el['title'])
        for ent in doc.ents:
            if ent.label_ == "GPE":
                if len(ent.text) > 0:
                    location = geocoder.geonames(ent.text, key=utils.GEONAMES_KEY)
                    details = geocoder.geonames(location.geonames_id, method='details', key=utils.GEONAMES_KEY)
                    location_data = {
                        "location": {
                            "name": ent.text,
                            "latitude": details.lat,
                            "longitude": details.lng
                        },
                        "image": el['image']
                    }
                    locations.append(location_data)
                break
    return locations
