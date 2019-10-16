#!/usr/bin/env python3
'''
A module for player classes
'''

class Player(object):
    '''
    A class representing an MLB Player
    '''
    def __init__(self, player):
        '''
        Constructor
        '''
        self.id = int(player['id'])
        self.name_first = player['first']
        self.name_last = player['last']
        self.name_display = player['name_display_roster']
