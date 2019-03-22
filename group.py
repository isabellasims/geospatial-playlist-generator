import numpy as np


class Group:
    
    
    def __init__(self, individuals, vectors):
        self.individuals = individuals
        self.vectors = vectors
    
    
    def separateGroup(self):
        """ Separate group into subgroups based on Euclidian distances. """
        for vector in self.vectors:
            
    
    def createPlaylist(self):
        """ group by common artists in playlists
            compare every song list with eachother to compute relationships
            each group must have a minimum of 10 common artists
            one group represented by each song generation
            if there are no groups
            implies small group with no shared preferences
            one individual represented by each song generation
            make playlist for each group (or individual) with common artists' songs"""
            
        subgroups = separateGroup()
