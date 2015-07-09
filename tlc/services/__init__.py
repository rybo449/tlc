class BaseService(object):
    def __init__(self, *args, **kwargs):
        pass

    def posts_in_new_york(self):
        raise NotImplementedError

    def location(self, **args):
        raise NotImplementedError

    def hashtag(self, **args):
        raise NotImplementedError

    def search_user(self, **args):
        raise NotImplementedError

    def top_locations(self, **args):
        raise NotImplementedError

    def get_tags(self, **args):
        raise NotImplementedError
