import random

from player import generate_player
from team import League, Team


def main():
    # set up the data
    # set up 8 teams
    # only one manager per team
    # only one league

    players = []
    for i in range(100):
        players.append(generate_player())

    # more teams will be added later on
    teams = [
        Team('Toronto Raptors'),
        Team('Los Angeles Lakers'),
        Team('Houston Rockets'),
        Team("Golden State Warriors"),
        Team('Oklahoma City Thunder'),
        Team('Philadelphia 76ers'),
        Team('Portland Trail Blazers'),
        Team('Milwaukee Bucks')
    ]

    for team in teams:
        # give them 5 starting players
        for player_num in range(5):
            selected_player = random.choice(players)
            team.players.append(selected_player)
            players.remove(selected_player)

    # one league
    first_league = League('NBA')
    first_league.set_teams(teams)


if __name__ == '__main__':
    main()
