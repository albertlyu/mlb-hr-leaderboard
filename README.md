# mlb-hr-leaderboard

## Overview
A Python project to display MLB homerun leaderboards using MLB Gameday JSON APIs

## Usage:
- Open a Terminal window at the root of this project
- `python3 main.py --season 2019 --month 7` for an MLB homerun leaderboard for July 2019
- `python3 main.py --season 2019 --month 6 --month_end 7` for an MLB homerun leaderboard for the range of June-July 2019
- `python3 main.py --season 2019` for an MLB homerun leaderboard for the 2019 season (Note: will take a long time)

## To Do:
- [x] Set up main runner for getting URLs for scoreboard JSON
- [x] Main runner to accept args for season and month (require season)
- [x] Traverse through days within month (use datetime to find dates in month-year)
- [x] For each master_scoreboard.json found, find the games
- [x] For each game found on the scoreboard, find the homeruns hit
- [x] For each new player found, track in PlayerStatsTracker
- [x] Keep track of players found in Players instance
- [x] Keep track of the number of homeruns hit by player ID in PlayerStatsTracker instance
- [x] Print HR leaderboard to output

## Improvements:
- [ ] Find a more accurate source for home run logs! (see [bug #1](https://github.com/albertlyu/mlb-hr-leaderboard/issues/1))
- [ ] Testing framework
- [ ] Thread scoreboard requests

## Credit:
- MLBAM for providing the data for this project
