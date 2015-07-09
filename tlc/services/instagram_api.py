from instagram.client import InstagramAPI

from . import BaseService
from tlc.settings.common import DATASOURCES
from NYC import zips


class InstagramService(BaseService):
    def __init__(self):
        client_id, client_secret = DATASOURCES['instagram']['client_id'], DATASOURCES['instagram']['client_secret']
        self.api = InstagramAPI(client_id=client_id, client_secret=client_secret)

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

    def search_user(self, user_id):
        pass

    def top_locations(self, lat, lng):
        pass

    def get_tags(self, url):
        pass
