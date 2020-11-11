import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# don't forget to set env variables SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET
auth_manager = SpotifyClientCredentials()

sp = spotipy.Spotify(auth_manager=auth_manager)

# user_id can be found in the settings of your account
playlists = sp.user_playlists('1156896537')
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s" % (i + 1 + playlists['offset'], playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
