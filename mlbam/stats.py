#!/usr/bin/env python3
'''
A module for stats classes
'''
from mlbam.player import Player

class PlayerStatsTracker(object):
    '''
    A class representing a stats tracker of player stats
    '''
    def __add_player_bio(self, player):
        '''
        Add player's bio to the stats tracker
        @param {dict} player
        '''
        self.players[int(player['id'])] = Player(player)

    def add_player_homeruns(self, player_homeruns):
        '''
        Add a player's homeruns for a game hit to the stats tracker
        @param {dict} player_homeruns
        '''
        # Create a key for homeruns in the stats tracker if it doesn't exist
        if not self.player_stats.get('homeruns'):
            self.player_stats['homeruns'] = dict()
        
        if player_homeruns.get('id'):
            player_id = int(player_homeruns.get('id'))

            # Create a player key for the homeruns stats tracker if it doesn't exist
            if not self.player_stats['homeruns'].get(player_id):
                self.player_stats['homeruns'][player_id] = 0

            # Track player bio if it is not already tracked
            if not self.players.get(player_id):
                self.__add_player_bio(player_homeruns)
            
            # If there are homeruns to add, add to stats tracker
            if player_homeruns.get('hr'):
                self.player_stats['homeruns'][player_id] = self.player_stats['homeruns'][player_id] + int(player_homeruns.get('hr'))

    def __init__(self):
        '''
        Constructor
        '''
        self.players = dict()
        self.player_stats = dict()
