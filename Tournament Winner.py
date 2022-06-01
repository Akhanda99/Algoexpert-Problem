def tournamentWinner(competitions, results):
    # Write your code here.
    point={}
    for i in range(0,len(competitions)):
        if results[i]==1:
            team=competitions[i][0]
        else:
            team=competitions[i][1]
        if team not in point:
            point.update({team: 0})
        point[team]+=3

        max=-9999
        for key, value in point.items():
            if value>max:
                max=value
                maxTeam=key
    return maxTeam

#test case 01:
competitions= [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
  ]
results= [0, 0, 1]
print(tournamentWinner(competitions, results))

#test case 02:
competitions1= [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"],
    ["C#", "Python"],
    ["Java", "C#"],
    ["C#", "HTML"]
  ]
results1= [0, 1, 1, 1, 0, 1]
print(tournamentWinner(competitions1, results1))