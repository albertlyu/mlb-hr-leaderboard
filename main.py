#!/usr/bin/env python3
'''
A main runner for accessing MLBAM data
'''
import argparse
from datetime import date, timedelta

from mlbam import gameday, stats, utils

parser = argparse.ArgumentParser(description='Access some MLBAM data')
parser.add_argument('--season',    help='MLB season, e.g. 2019',       type=int, required=True)
parser.add_argument('--month',     help='Month within season, e.g. 7', type=int, required=False)
parser.add_argument('--month_end', help='Month end of season, e.g. 9', type=int, required=False)

def main():
    '''
    The main entrypoint for accessing MLBAM scoreboard JSON
    '''
    args = parser.parse_args()
    
    season = args.season
    month_start = args.month or args.month_end or 3 # assume the earliest regular season date is in Mar
    month_end = args.month_end or args.month or 11  # assume the latest regular season date is in Oct

    if month_start and month_end and month_end < month_start:
        raise ValueError('Please re-enter a month and month_end where month_end is later than the month. month: ' + str(args.month) + ', month_end: ' + str(args.month_end))

    # After the args are parsed, make a list of game dates
    game_date_start = date(season, month_start, 1)
    game_date_end = utils.last_date_of_month(date(season, month_end, 1))
    game_dates = [game_date_start + timedelta(days=x) for x in range((game_date_end-game_date_start).days+1)]

    mlbam_reader = gameday.MlbamGamedayReader()
    stats_tracker = stats.PlayerStatsTracker()

    # Start getting player homeruns for them game dates, and add to stats tracker
    for game_date in game_dates:
        player_homeruns_for_game_date = mlbam_reader.get_player_homeruns_for_game_date(game_date)
        if player_homeruns_for_game_date:
            for player_homeruns in player_homeruns_for_game_date:
                stats_tracker.add_player_homeruns(player_homeruns)

    # Get the final homerun leaderboard!
    homerun_leaderboard = stats_tracker.get_homerun_leaderboard()

    for homerun_line in homerun_leaderboard:
        print(homerun_line[0] + ' ' + homerun_line[1] + ' ' + str(homerun_line[2]))

if __name__ == '__main__':
    main()
