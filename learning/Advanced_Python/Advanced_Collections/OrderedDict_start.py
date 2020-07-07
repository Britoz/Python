# Demonstrate the usage of OrderedDict objects
from collections import OrderedDict

def main():
    # list of sport teams with wins and losses
    sportTeams = [("Rovals", (18, 12)), ("Rockets", (24, 6)),
                  ("Lee", (20, 10)), ("Marvel", (11, 12)),
                  ("Fire", (22, 32)), ("Fox", (13, 32)),
                  ("Team", (54, 12)), ("New", (42, 12))]

    '''
    each team has their win and loss record
    '''

    # sort the teams by number of wins
    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)
    '''
    sorted(array, key of sorted, checking reverse or not
    t[1][0] is getting the first value which is win element
    
    '''

    # TODO: create an ordered dictionary of the teams
    teams = OrderedDict(sortedTeams)
    print(teams)

    # TODO: Use popitem to remove the top iteam
    tm, wl = teams.popitem(False)
    print("Top team: ", tm, wl)

    # TODO: what are next the top 4 teams?
    # run a loop with index and mix by enumerate and start index with 1
    for i, team in enumerate(teams, start=1):
        print(i, team)
        if i == 4:
            break

    # TODO: test for equality
    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "b": 2, "c": 2})
    print("Equality test: ", a == b)

if __name__ == '__main__':
    main()