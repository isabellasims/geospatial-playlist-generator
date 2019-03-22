import spotipy
import spotipy.util as util
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%
# connecting script to Spotify Application
CLIENT_ID = '...'
CLIENT_SECRET = '...'
USERNAME = '...'
REDIRECT_URI = 'https://google.com'
SCOPE = 'user-library-read playlist-read-private'

# asks user to input token ("google.com") for authentication
token = util.prompt_for_user_token(username=USERNAME,
                                   scope=SCOPE,
                                   client_id=CLIENT_ID,
                                   client_secret=CLIENT_SECRET,
                                   redirect_uri=REDIRECT_URI)


def get_features(connection, username, playlist_id):
    """Returns a pandas dataframe of audio features every song in playlist
    object, up to 100 songs. Function takes three arguments: 
    Spotify connection object (variable name), Spotify username (string), and
    playlist ID (string)."""
    song_ids = []
    playlist = connection.user_playlist(username, playlist_id)
    tracks = playlist['tracks']
    for item in tracks['items']:
        song_ids.append(item['track']['id'])
    # extracting audio features from 50 songs at a time
    features = []
    for i in range(0,len(song_ids),50):
        audio_features = connection.audio_features(song_ids[i:i+50])
        for track in audio_features:
            features.append(track)
    # creating dataframe with each song's features
    return pd.DataFrame(features)


if token:
    # instantiating Spotify API connection object
    sp = spotipy.Spotify(auth=token)

    # growing list of playlist dataframes
    playlists = sp.user_playlists(USERNAME)
    good_playlists = []
    for playlist in playlists['items']:
        playlist_id = str(playlist['external_urls']).split("'")[3].split("/")[4]
        good_playlists.append(get_features(sp,USERNAME,playlist_id))
    good_songs = pd.concat(good_playlists)
    
else:
    print("Cannot retrieve token for ", username)

