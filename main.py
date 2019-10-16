#!/usr/bin/env python3
'''
A main runner for accessing MLBAM data
'''
import argparse

from mlbam import gameday

parser = argparse.ArgumentParser(description='Access some MLBAM data')
parser.add_argument('--season', help='MLB season, e.g. 2019',      type=int, required=True)
parser.add_argument('--month',  help='Month within season, e.g. 7', type=int, required=False)

def main():
    '''
    The main entrypoint for accessing MLBAM scoreboard JSON
    '''
    print('hello world')

    args = parser.parse_args()
    
    print(args.season)
    print(args.month)


if __name__ == '__main__':
    main()
