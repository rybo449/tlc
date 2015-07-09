from instagram.client import InstagramAPI
from . import BaseService
from settings.common import DATASOURCES


class InstagramService(BaseService):
    def __init__(self):
        client_id, client_secret = DATASOURCES['instagram']['client_id'], DATASOURCES['instagram']['client_secret']
        self.api = InstagramAPI(client_id=client_id, client_secret=client_secret)

    def location(self, lat, lng):
        data = []
        return
