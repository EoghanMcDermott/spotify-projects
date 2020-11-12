import spotipy
from spotipy.oauth2 import SpotifyOAuth

import config

auth_manager = SpotifyOAuth(config.client_id, config.client_secret, redirect_uri=config.redirect_uri, scope=config.scope)

sp = spotipy.Spotify(auth_manager=auth_manager)

artists = sp.current_user_top_artists(limit=20, time_range='short_term')

for i, artist in enumerate(artists['items']):
    print("%4d %s" % (i + 1 + artists['offset'], artist['name']))

