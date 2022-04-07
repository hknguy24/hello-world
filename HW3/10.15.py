# Huy Kevin Nguyen
# PSID: 1346435

class Team:
    def __init__(self):
        self.teamname = 'none'
        self.teamwins = 0.0
        self.team_losses = 0.0

    def get_win_percentage(self):
        return self.teamwins / (self.teamwins + self.team_losses)

if __name__ == "__main__":
    n = input()
    w = float(input())
    l = float(input())
    s = Team()
    s.teamname = n
    s.teamwins = w
    s.team_losses = l
    if s.get_win_percentage() >= 0.5:
        print('Congratulations, Team', s.teamname, 'has a winning average!')
    else:
        print('Team', s.teamname, 'has a losing average.')