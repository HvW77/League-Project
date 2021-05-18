import re
from collections import defaultdict

file_path = 'teams.txt'
file = open(file_path, 'r')
league_table = defaultdict(lambda: {"points": 0})

# Points allocation calc of team1 and team2
def calc_points(team1, team2, score1, score2):
    if score1 == score2:
        return {team1: 1, team2: 1}
    if score1 > score2:
        return {team1: 3, team2: 0}
    if(score1 < score2):
        return {team1: 0, team2: 3}

# Ranking position
def pos_num(pos):
    return {1: "st", 2: "nd", 3: "rd", 21: "st", 22: "nd", "23": "rd"}.get(pos, "th")

def table():
    teams1 = ()
    teams2 = ()
    scores1 = ()
    scores2 =()
    i = 0

    # Iterate through txt file
    for lines in file:
        data = lines.split(",") # Seperator
        teams1 += re.search("(\S+.*?)\s+\d+\s*$", data[0]).group(1), # Only get String
        scores1 += int(re.search("(\d+)\s*$", data[0]).group(1)), # Only get Int
        teams2 += re.search("(\S+.*?)\s+\d+\s*$", data[1]).group(1), # Only get String
        scores2 += int(re.search("(\d+)\s*$", data[1]).group(1)), # only get Int

        match_outcome = calc_points(teams1[i], teams2[i], scores1[i], scores2[i])

        # Allocate names and points
        league_table[teams1[i]] = {
                        "name": teams1[i],
                        "points": league_table[teams1[i]]["points"] + match_outcome[teams1[i]]
                    }
        league_table[teams2[i]] = {
                        "name": teams2[i],
                        "points": league_table[teams2[i]]["points"] + match_outcome[teams2[i]]
                    }
        i = i + 1

    return sorted(league_table.values(), key=lambda x: (-x["points"])) # sort table by most points

# Output
for i, team in enumerate(table()):
    pos = f"{i + 1}{pos_num(i+1)}:".center(6)
    name = f"{team['name']}".center(30)
    points = f"{team['points']} pts".center(6)
    print(pos, name, points)

file.close()