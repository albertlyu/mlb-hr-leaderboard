#!/usr/bin/env python3
'''
A module for reading MLBAM Gameday files
'''
import requests
import time

BASE_URL = "https://gd2.mlb.com/components/game/mlb"
SCOREBOARD_FILE_NAME = 'master_scoreboard.json'

class MlbamGamedayReader(object):
    '''
    A class for reading MLBAM Gameday data
    '''
    def __get_gameday_json(self, game_date, json_file_name):
        '''
        Private method to get JSON content from MLBAM's Gameday directory for a game date, if it exists
        @param  {datetime.date} game_date - displays as YYYY-MM-DD
        @param  {string}        json_file_name - e.g. master_scoreboard.json
        @return {dict}
        '''
        year = game_date.year
        month = game_date.month
        day = game_date.day
        gameday_json_url = BASE_URL + "/year_%s/month_%02d/day_%02d/%s" % (year, month, day, json_file_name)
        
        response = requests.get(gameday_json_url)
        time.sleep(0.1)  # being nice
        
        if response.status_code == 200:
            return response.json().get('data')
        else:
            print('Error accessing %s: HTTP code %s -- skipping' % (gameday_json_url, response.status_code))
            return
    
    def __get_games_from_json(self, scoreboard_json):
        '''
        Private method to get the games from a scoreboard JSON object as it is received from MLBAM's Gameday 
        directory from the scoreboard JSON API. Represented as a Python dictionary
        @param  {dict} scoreboard_json
        @return {dict}
        '''
        try:
            return scoreboard_json.get('games').get('game')
        except AttributeError:
            print('Error accessing games in master scoreboard JSON object, exiting!')
            return

    def __get_player_homeruns_from_game(self, game_json):
        '''
        Private method to get players who hit homeruns in a game JSON object. Represented as a Python dictionary.
        @param  {dict} game_json
        @return {dict}
        '''
        try:
            return game_json.get('home_runs')
        except AttributeError:
            print('Error accessing games in master scoreboard JSON object, exiting!')
            return
    
    def get_player_homeruns_for_game_date(self, game_date):
        '''
        Public method to get the player-homeruns for a game date
        @param  {datetime.date} game_date
        @return {list<dict>}
        '''
        # Get games for the game date provided
        game_date_data = self.__get_gameday_json(game_date, SCOREBOARD_FILE_NAME)
        games = self.__get_games_from_json(game_date_data)
        if not games or not isinstance(games, list):
            print('No games found on %s -- passing' % (game_date,))
            return
    
        # For each game, find player homeruns, and make a list of them
        total_player_homeruns = []
        for game in games:
            player_homeruns = self.__get_player_homeruns_from_game(game)
            if not player_homeruns or not player_homeruns.get('player'):
                print('No homeruns found for %s -- passing' % (game.get('gameday'),))
                continue
            if isinstance(player_homeruns.get('player'), list):
                total_player_homeruns.extend(player_homeruns.get('player'))
            else:
                # if only one player hit homeruns in the game, its an object! oof...
                total_player_homeruns.append(player_homeruns.get('player'))

        return total_player_homeruns
        