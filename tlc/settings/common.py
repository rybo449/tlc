from . import secret

DATASOURCES = {
    'instagram': dict(
        client_id= secret.INSTAGRAM_CLIENT_ID,
        client_secret= secret.INSTAGRAM_CLIENT_SECRET,
    ),
    'clarifai': dict(
        app_id= secret.CLARIFAI_APP_ID,
        app_secret= secret.CLARIFAI_APP_SECRET,
    ),
    'googlemaps': dict(
        key= secret.GOOGLEMAPS_CLIENT_KEY,
    ),
    'twitter': dict(
        api_key=secret.TWITTER_API_KEY,
        api_secret=secret.TWITTER_API_SECRET,
        access_token=secret.TWITTER_ACCESS_TOKEN,
        access_token_secret=secret.TWITTER_TOKEN_SECRET,
    ),
    'foursquare': dict(
        client_id=secret.FOURSQUARE_CLIENT_ID,
        client_secret=secret.FOURSQUARE_CLIENT_SECRET,
    ),
    'uber': dict(
        client_id = secret.UBER_CLIENT_ID,
        secret=secret.UBER_SECRET,
        server_token = secret.UBER_SERVER_TOKEN,
    ),
    'factual': dict(
        app_id = secret.FACTUAL_APP_ID,
        app_secret = secret.FACTUAL_APP_SECRET,
    ),
}