"""
-League
  -Teams
    -Manager
    -Players
      -Skill/Overall
      -Salary
"""
import copy
import random


class Game:
    """
    Teams play against each other
    Game is in league
    """
    def __init__(self, league, home_team, away_team):
        self.league = league

        self.home_team = home_team
        self.away_team = away_team

        print('{} vs {}'.format(self.home_team, self.away_team))

    def play(self):
        """
        Play the game, return who won
        True means home team won, False means away team won
        """
        print('The game has now begun...')

        print('Game\'s over fellas.')
        print('Home team wins the game')
        return True

class League:
    """
    Has different teams that consists in it
    Each team has a ranking
    """
    def __init__(self, name):
        self.name = name
        self.teams = []


    def set_teams(self, teams):
        self.teams = teams

    def play_seasons(self):
        """
        play 30 games in the regular season
        """
        for i in range(30):
            self.play_regular_games()

    def play_playoffs(self):
        """
        8 teams play for the championship
         -First round  8
          -Semi Finals 4
           -The Finals 2
             -Winner   1
        """
        num_teams = len(self.teams)
        num_games = num_teams/2

        teams_to_play = copy.copy(self.teams)

        for game_num in range(num_games):
            home_team = random.choice(teams_to_play)
            teams_to_play.remove(home_team)
            away_team = random.choice(teams_to_play)
            teams_to_play.remove(away_team)

            game = Game(self, home_team, away_team)
            winner = game.play()

            if winner:
                #home team won
                home_team.wins += 1
                away_team.losses += 1
            else:
                #away team won
                away_team.wins += 1
                home_team.losses += 1

class Team:
    """
    Consists of many players
    Teams play against each other
    Has one manager
    Has ranking in league
    """
    def __init__(self, name):
        self.name = name
        self.players = []

        self.wins = 0
        self.losses = 0

class Manager:
    """
    Runs the team
    Can trade/let go of players
    """
    pass
