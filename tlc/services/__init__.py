from tlc.settings.common import DATASOURCES
from NYC import zips
from clarifai.client import ClarifaiApi
from instagram.client import InstagramAPI
import googlemaps
from factual import Factual
from factual.utils import circle
import tweepy


class Geocode(object):
    def __init__(self):
        self.gmaps = googlemaps.Client(key=DATASOURCES['googlemaps']['key'])

    def geocode(self, place):
        geocode = self.gmaps.geocode(place)
        return geocode[0][u'geometry'][u'location'][u'lat'], geocode[0][u'geometry'][u'location'][u'lng']

    def reverse_geocode(self, lat, lng):
        geocode = self.reverse_geocode((lat, lng))
        return geocode[0][u'formatted_address']


class InstagramService(object):
    def __init__(self):
        client_id, client_secret = DATASOURCES['instagram']['client_id'], DATASOURCES['instagram']['client_secret']
        self.api = InstagramAPI(client_id=client_id, client_secret=client_secret)
        app_id, app_secret = DATASOURCES['clarifai']['app_id'], DATASOURCES['clarifai']['app_secret']
        self.image_api = ClarifaiApi(app_id=app_id, app_secret=app_secret)
        factual_id, factual_secret = DATASOURCES['factual']['app_id'], DATASOURCES['factual']['app_secret']
        places = Factual(factual_id, factual_secret)
        self.places = places.table('places')

    def posts_in_new_york(self):
        media = []

        for row in zips:
            lat, lng = float(row[0]), float(row[1])
            posts = self.api.media_search(lat=lat, lng=lng, distance=800)
            for post in posts:
                temp_list = [post.id, post.images['standard_resolution'].url, post.created_time,
                             post.location.point.latitude, post.location.point.longitude]
                media.append(temp_list)
                print temp_list
        return media

    def location(self, lat, lng):
        posts = self.api.media_search(lat=lat, lng=lng, distance=800)
        media = []
        for post in posts:
            temp_list = [post.id, post.images['standard_resolution'].url, post.created_time,
                         post.location.point.latitude, post.location.point.longitude]
            media.append(temp_list)
            print temp_list
        return media

    def hashtag(self, lat, lng):
        posts = self.api.media_search(lat=lat, lng=lng, distance=800)
        hashtags = {}
        for post in posts:
            tokens = str(post.caption).split(' ')
            for token in tokens:
                if token and len(token) > 1:
                    if token[0] == '#':
                        count = hashtags.setdefault(token, 0)
                        hashtags[token] = count + 1
                    elif token[0] == '"' and token[1] == '#':
                        count = hashtags.setdefault(token[1:], 0)
                        hashtags[token[1:]] = count + 1
        return hashtags

    def get_landmarks(self, lat, lng):
        data = self.places.geo(circle(lat, lng, 800)).data()
        return data

    def get_tags(self, place):
        tags = {}
        lat, lng = Geocode().geocode(place)
        posts = self.api.media_search(lat=lat, lng=lng, distance=800)
        for post in posts:
            result = self.image_api.tag_image_urls(post.images['standard_resolution'].url)
            image_tags = result['results'][0]['result']['tag']['classes'][:5]
            for tag in image_tags:
                count = tags.setdefault(tag, 0)
                tags[tag] = count + 1
        return tags

class TwitterService(object):
    def __init__(self):
        auth = tweepy.OAuthHandler(DATASOURCES['twitter']['api_key'], DATASOURCES['twitter']['api_secret'])
        auth.set_access_token(DATASOURCES['twitter']['access_token'], DATASOURCES['twitter']['access_token_secret'])
        self.api = tweepy.API(auth)