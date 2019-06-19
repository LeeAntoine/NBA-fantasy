import random


class Player:
    """
    Plays in games for their team
    Has skill/overall
    Has a salary
    """

    def __init__(self, name, skill, salary):
        self.name = name
        self.salary = salary

        # skill/overall
        # generates the given overall of the player
        self.skill = skill

    def salary(self):
        return 50000 + self.skill * 100


def generate_player():
    player_names = [
        """
        Lebron James,
        Anthony Davis,
        Giannis Antetokounmpo,
        Danny Green,
        Stephen Curry,
        Klay Thompson,
        Kevin Durant,
        Demarcus Cousins,
        Damian Lillard,
        Kyrie Irving,
        Ben Simmons,
        Joel Embiid,
        Derrick Rose,
        Bradley Beal,
        John Wall,
        D'Angelo Russell,
        Victor Oladipo,
        CJ Mccollum,
        Lonzo Ball,
        Kemba Walker,
        Kawhi Leonard,
        Kyle Lowry,
        James Harden,
        Chris Paul,
        Russel Westbrook,
        Paul George,
        Jimmy Butler,
        Marc Gasol,
        Devin Booker,
        De'Aaron Fox,
        Al Horford,
        Blake Griffin,
        Andre Iguodala,
        Serge Ibaka,
        Jayson Tatum,
        Donovan Mitchell,
        Trae Young,
        Kyle Kuzma,
        Gordon Hayward,
        Karl Anthony Towns
        """
    ]
    player_name = random.choice(player_names)

    # generate overall and salary
    skill = 60 + random.randint(99)
    return Player(player_name, skill)
