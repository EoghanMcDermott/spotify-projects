import spotipy
from spotipy.oauth2 import SpotifyOAuth

import config

auth_manager = SpotifyOAuth(config.client_id, config.client_secret, redirect_uri=config.redirect_uri, scope=config.scope)

sp = spotipy.Spotify(auth_manager=auth_manager)

playlists = sp.user_playlists(config.username)
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s" % (i + 1 + playlists['offset'], playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
