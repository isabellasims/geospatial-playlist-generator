import spotipy
import spotipy.util as util
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Individual:
    
    
    def __init__(self, username, client_id, client_secret):
        """ Takes three constructor arguments: username, client_id, client_secret. """
        self.username = username
        self.id = client_id
        self.secret = client_secret
    
    
    def connect(self):
        """ Returns connection object if able to establish connection to Spotify API. """
        token = util.prompt_for_user_token(username=self.username,
                                           scope='user-library-read playlist-read-private',
                                           client_id=self.id,
                                           client_secret=self.secret,
                                           redirect_uri='https://google.com')
        if token:
            return spotipy.Spotify(auth=token)
        
        else:
            return 'Unable to establish connection.'
        
    
    def getPlaylistID(self, playlist):
        """ Returns ID of playlist passed object passed in. """
        return str(playlist['external_urls']).split("'")[3].split("/")[4]
        
        
    def getFeatures(self, connection, username, playlist_id):
        """Returns a pandas dataframe of audio features every song in playlist object, up to 100 songs.
        Function takes three arguments: Spotify connection object (variable name), Spotify username (string),
        and playlist ID (string)."""
        song_ids = []
        playlist = connection.user_playlist(self.username, playlist_id)
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
    
    
    def getDataFrame(self):
        """ Returns Pandas dataframe of all songs belonging to Individual object's playlists. 
        Takes no args. """
        sp = self.connect()
        playlists = sp.user_playlists(self.username)
        playlist_array = []
        for playlist in playlists['items']:
            playlist_id = self.getPlaylistID(playlist)
            playlist_array.append(self.getFeatures(sp,self.username,playlist_id))

        return pd.concat(playlist_array)
        
        
    def averageVector(self):
        """ Returns vector of average features for Individual's songs. """
        dataframe = self.getDataFrame()
        del dataframe['analysis_url'], dataframe['id'], dataframe['track_href'], dataframe['uri'], dataframe['type']
        return np.array([dataframe[feature].mean() for feature in dataframe])
        
