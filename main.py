#!/usr/bin/env python3
'''
A main runner for accessing MLBAM data
'''
import argparse
from datetime import date, timedelta

from mlbam import gameday, utils

parser = argparse.ArgumentParser(description='Access some MLBAM data')
parser.add_argument('--season',    help='MLB season, e.g. 2019',       type=int, required=True)
parser.add_argument('--month',     help='Month within season, e.g. 7', type=int, required=False)
parser.add_argument('--month_end', help='Month end of season, e.g. 9', type=int, required=False)

def main():
    '''
    The main entrypoint for accessing MLBAM scoreboard JSON
    '''
    args = parser.parse_args()
    
    month_start = args.month or args.month_end or 3 # assume the earliest regular season date is in Mar
    month_end = args.month_end or args.month or 11  # assume the latest regular season date is in Oct

    if month_start and month_end and month_end < month_start:
        raise ValueError('Please re-enter a month and month_end where month_end is later than the month. month: ' + str(args.month) + ', month_end: ' + str(args.month_end))

    game_date_start = date(args.season, month_start, 1)
    game_date_end = utils.last_date_of_month(date(args.season, month_end, 1))
    game_dates = [game_date_start + timedelta(days=x) for x in range((game_date_end-game_date_start).days+1)]

    mlbam_reader = gameday.MlbamGamedayReader()

    total_player_homeruns = mlbam_reader.get_player_homeruns(game_dates)

if __name__ == '__main__':
    main()
