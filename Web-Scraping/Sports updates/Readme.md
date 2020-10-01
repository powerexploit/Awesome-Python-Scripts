## Sports Score Updates
  - This script fetch the latest score for matches, team info and match info
  - This script supports:
    - baseball
    - basketball
    - cricket
    - football
    - handball
    - hockey
    - rugby-league
    - rugby-union
    - soccer
    - tennis
    - volleyball

  
## Setting up :
### Install requirements:
```sh
$ pip3 install sports-py
```

### Running the script:
```sh
# gets the live score:
$ python3 score_updates.py <sportName>
# gets the details of match between two teams:
$ python3 sports_score_updates.py <sportName> <team1> <team2>
# gets the details of a team:
$ python3 sports_score_updates.py <sportName> <teamName>
