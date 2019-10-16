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
        if 'homeruns' not in self.player_stats.keys():
            self.player_stats['homeruns'] = dict()
        
        if 'id' in player_homeruns.keys():
            player_id = int(player_homeruns.get('id'))

            # Create a player key for the homeruns stats tracker if it doesn't exist
            if player_id not in self.player_stats['homeruns'].keys():
                self.player_stats['homeruns'][player_id] = 0

            # Track player bio if it is not already tracked
            if player_id not in self.players.keys():
                self.__add_player_bio(player_homeruns)
            
            # If there are homeruns to add, add to stats tracker
            if 'hr' in player_homeruns.keys():
                self.player_stats['homeruns'][player_id] = self.player_stats['homeruns'][player_id] + int(player_homeruns.get('hr'))
    
    def get_homerun_leaderboard(self):
        '''
        Get the current homerun leaderboard
        @return {list<list>}
        '''
        hr_dict = self.player_stats['homeruns']
        hr_lines = []
        for player_id in hr_dict.keys():
            player = self.players[player_id]
            home_runs = hr_dict[player_id]
            hr_line = [player.name_first, player.name_last, home_runs]
            hr_lines.append(hr_line)
            
        hr_lines.sort(key=lambda x: x[2], reverse=True)
        return hr_lines

    def __init__(self):
        '''
        Constructor
        '''
        self.players = dict()
        self.player_stats = dict()
