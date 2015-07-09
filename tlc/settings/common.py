from . import secret

DATASOURCES = {
    'instagram': dict(
        client_id= secret.INSTAGRAM_CLIENT_ID,
        client_secret= secret.INSTAGRAM_CLIENT_SECRET,
    ),
}