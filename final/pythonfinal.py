from tkinter import *
import csv

'''class fantasy_teams:

    def __init__(self, master):
        self.master = master
        master.title("Enter teams")

        self.team = '\n'
        self.entered_team = ''
        
        self.team_txt = StringVar()
        self.team_txt.set(self.team)
        self.team_label = Label(master, textvariable=self.team_txt)
        
        self.label = Label(master, text='Teams:')

        vcmd = master.register(self.validate)
        self.entry = Entry(master, validate='key', validatecommand=(vcmd, '%P'))

        self.team_button = Button(master, text='ENTER', command=lambda: self.update())
        self.done_button = Button(master, text='DONE', command=self.master.destroy)
        
        self.label.grid(row=0, column=0, sticky=W)
        self.team_label.grid(row=0, column=1, columnspan=2, sticky=E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.team_button.grid(row=2, column=0)
        self.done_button.grid(row=2, column=1)

    def validate(self, new_text):
        teams = {}
        if not new_text:
            self.entered_team = ''
            return True
        self.entered_team = new_text
        teams[new_text] = []
        print(teams)
        return teams
    def update(self):
        self.team = self.entered_team

        self.team_txt.set(self.team)
        self.entry.delete(0, END)

root = Tk()
my_qui = fantasy_teams(root)
root.mainloop()
'''




class makin_teams:
    def __init__(self, master):
        self.teams = {}
        self.person = {}
        self.master = master
        self.label_1 = Label(master, text='Name')
        self.label_2 = Label(master, text='Team')

        self.team_name = StringVar()
        self.name_name = StringVar()
        
        self.entry_1 = Entry(master, textvariable=self.name_name)
        self.entry_2 = Entry(master, textvariable=self.team_name)

        self.button_1 = Button(
            master, text='ENTER', command=lambda :self.add_team())
        self.button_2 = Button(master, text='DONE', command=self.master.destroy)

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)

        self.button_1.grid(row=2)
        self.button_2.grid(row=2, column=1)

        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)

    def add_team(self):
        try:
            self.person[self.name_name.get()] = []
            self.entry_1.delete(0, END)
        except:
            pass
        return self.person

    def done(self):
        self.master.destroy

root = Tk()
teamers = makin_teams(root)
root.mainloop()
teams = teamers.add_team()
print('finally',teams)

#basics start here
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
