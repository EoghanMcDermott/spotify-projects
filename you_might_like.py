import spotipy
from spotipy.oauth2 import SpotifyOAuth

import config

auth_manager = SpotifyOAuth(config.client_id, config.client_secret, redirect_uri=config.redirect_uri, scope=config.scope)

sp = spotipy.Spotify(auth_manager=auth_manager)

artists = sp.current_user_top_artists(limit=20, time_range='short_term')

for i, artist in enumerate(artists['items']):
    similar_artists = sp.artist_related_artists(artist['id'])
    for similar in enumerate(similar_artists):
        print(similar)
