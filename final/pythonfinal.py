import csv

teams = {}
while True:
    team_name = input('enter team name - q to quit.\n')
    if team_name == 'q':
        break
    else:
        teams[team_name] = []
        continue
print(teams)
'''with open('players.csv') as csvfile:
    readcsv = csv.reader(csvfile, delimiter=',')
    for row in readcsv:
        name = row[0]
        first_name = row[1]
        last_name = row[2]
        college = row[7]
        print(row)
        print(row[0])
        print(row[0], row[1], row[2])
'''
draft_order = []
print('Please set the draft order\n')
for team in teams:
    print(team)

i = 0

while i < len(teams):
    draft_team = input('please enter team in draft position #%d\n' % (i+1))
    if draft_team not in teams:
        print('team not found')
        continue
    else:
        draft_order.append(draft_team)
        i += 1
        continue
print(draft_order)

print('let the draft begin!')
turn = 0
while True:
    print('turn =', turn)
    player = input('who will %s draft?\n' % draft_order[turn])
    if player == 'done':
        break
    else:
        teams[draft_order[turn]].append(player)
        turn += 1
        if turn >= len(teams):
            print('triggered')
            turn = turn % len(teams)
            continue
print(teams)
