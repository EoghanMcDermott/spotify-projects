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

#### Sample Output:
      1 when you get given the AUX at a party 
      2 car bops
      3 mildly obscure japanese music to existentially vibe to
      4 lofi hip hop music - beats to relax/study to
      5 NEO POP COMPLEχ
      6 The Sound of Japanese Shoegaze
      7 Objectively Class Tunes
      8 HangaR2.0
      9 A Breath of Fresh Éire
     10 Discover Weekly

## top_recent_artists
Prints a user's recent top 20 most listened to artists

#### Sample Output:
     1 Explosions In The Sky
     2 Covet
     3 Haru Nemuri
     4 百景
     5 Vince Staples
     6 April
     7 The Story So Far
     8 Charli XCX
     9 Against All Logic
    10 Taeko Onuki
    11 100 gecs
    12 Candy Claws
    13 Bon Iver
    14 Playboi Carti
    15 Lorde
    16 yuragi
    17 Have A Nice Life
    18 Rina Sawayama
    19 The World Is A Beautiful Place & I Am No Longer Afraid To Die
    20 City Girl
