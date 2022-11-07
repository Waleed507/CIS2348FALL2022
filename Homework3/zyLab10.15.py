# Waleed Yusuf
# 2104654

class Team:
    def __init__(self, name='None', wins=0, losses=0):
        self.team_name = name
        self.team_wins = wins
        self.team_losses = losses

    def get_win_percentage(self):
        return self.team_wins / (self.team_wins + self.team_losses)


if __name__ == "__main__":

    team = Team()

    team_name = input()
    team_wins = int(input())
    team_losses = int(input())

    team.team_name = team_name
    team.team_wins = team_wins
    team.team_losses = team_losses

    if team.get_win_percentage() >= 0.5:
        print(f'Congratulations, Team {team.team_name} has a winning average!')
    else:
        print(f'Team {team.team_name} has a losing average.')
