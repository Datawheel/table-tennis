# elo function
#
k = 25

def winner_function (team_1_score, team_2_score):
    if team_1_score > team_2_score:
        win=1
    else:
        win=0

def elo (team_1_elo, team_2_elo, win):
    rating = 1.0/ (1.0 + 10.0**((team_2_elo-team_1_elo)/400.0))
    return team_1_elo + (k * (win-rating))


print elo (1200, 1250, 1)


# import csv

# ofile = open('test.csv', "rb")
# reader = csv.reader(ofile)
# zero = 0
# for row in reader:
#     if zero == 0:
#         head = row
#     else:
#         co
