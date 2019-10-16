# mlb-hr-leaderboard

## Overview
A Python project to display MLB homerun leaderboards using MLB Gameday JSON APIs

## To Do:
- [x] Set up main runner for getting URLs for scoreboard JSON
- [x] Main runner to accept args for season and month (require season)
- [x] Traverse through days within month (use datetime to find dates in month-year)
- [x] For each master_scoreboard.json found, find the games
- [x] For each game found on the scoreboard, find the homeruns hit
- [x] For each new player found, track in PlayerStatsTracker
- [x] Keep track of players found in Players instance
- [x] Keep track of the number of homeruns hit by player ID in PlayerStatsTracker instance
- [ ] Print HR leaderboard to output

## Improvements:
- [ ] Testing framework
