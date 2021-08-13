import sports
import sys

sdict = {
    'baseball': sports.BASEBALL,
    'basketball': sports.BASKETBALL,
    'cricket': sports.CRICKET,
    'football': sports.FOOTBALL,
    'handball': sports.HANDBALL,
    'hockey': sports.HOCKEY,
    'rugby-league': sports.RUGBY_L,
    'rugby-union': sports.RUGBY_U,
    'soccer': sports.SOCCER,
    'tennis': sports.TENNIS,
    'volleyball': sports.VOLLEYBALL
}

arguments = sys.argv
if (len(arguments) < 2):
    print('Please enter a sport as a argument we support these sports.')
    for a in sdict.keys():
    	print(a)
    exit()

if (len(arguments) == 2):
    sport = arguments[1].lower()
    if sport in sdict.keys():
        all_matches = sports.all_matches()[sport]
        for match in all_matches:
            print(match)
    else:
        print('This sport details are not supported yet')

if (len(arguments) == 3):
    sport = arguments[1].lower()
    if (sport == 'baseball' or sport == 'basketball' or sport == 'football' or sport == 'hockey'):
        sport = sdict.get(sport)
        team = arguments[2].lower()
        team_info = sports.get_team(sport, team)
        print(team_info)
    else:
        print('This sport details are not supported yet')

if (len(arguments) == 4):
    sport = arguments[1].lower()
    if sport in sports_dict.keys():
        sport = sports_dict.get(sport)
        team1 = arguments[2].lower()
        team2 = arguments[3].lower()
        match_info = sports.get_match(sport, team1, team2)
        print(match_info)
    else:
        print('This sport details are not supported yet')
