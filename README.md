# Spotify Projects using spotipy library & Spotify API

## Prerequisites
First, make sure to install spotipy

`pip install spotipy --upgrade` 

You also need to create an app on your [Spotify Dashboard](https://developer.spotify.com/dashboard)

Once your app is created, you will need to go to <b>Edit Settings</b> and add a <b>Redirect URI</b>

It doesn't have to be an actual website, e.g. I am using `http://localhost:8080` - take note of this value

From here, also note the <b>client ID</b> and <b>client secret</b> values
 
Then make sure to set these values in your config file

For now, you also need to enter your username in your config file, which can be found [here](https://www.spotify.com/account/overview/)


## print_playlists
Prints a user's saved playlists

## top_recent_artists
Prints a user's recent top 20 most listened to artists
