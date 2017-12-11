from tkinter import *
import csv
from functools import partial

#add teams gui
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

        self.entry_1.bind('<Return>', self.button_focus)
        self.entry_2.bind('<Return>', self.add_team)
        self.button_1.bind('<Return>', self.add_team)
        self.button_2.bind('<Return>', self.main_destroy)

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)

        self.button_1.grid(row=2)
        self.button_2.grid(row=2, column=1)

        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)

        self.entry_1.focus()

    def button_focus(self, master):
        self.entry_2.focus()

    def add_team(self, master=0):
        try:
            self.person[self.team_name.get()] = self.name_name.get()
            self.teams[self.team_name.get()] = []
            self.entry_1.focus()
            self.entry_1.delete(0, END)
            self.entry_2.delete(0, END)
        except:
            pass
        return self.teams, self.person

    def main_destroy(self, thing):
        self.master.destroy()


#set teams in desired draft order
class draft_orderin:
    def __init__(self, master):
        self.order = []
        self.master = master
        self.button_identities = []
        self.label = Label(master, text='choose the draft order')
        self.label.pack()
        for i,team in enumerate(teams):
            self.button = Button(master, text=team, command=partial(self.store, i, team))
            self.button.pack()
            self.button_identities.append(self.button)

        self.done_button = Button(master, text='DONE', command=self.master.destroy)
        self.done_button.pack()

    def store(self, i, team):
        self.order.append(team)
        self.bname = (self.button_identities[i])
        self.bname.destroy()

    def order_return(self):
        return self.order


#import all the current relevant players and store in dictionary name:[team, position]
def playercsv():
    player = {}
    with open('players2017.csv') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=',')
        for row in readcsv:
            player[row[1]+' '+row[3] +' '+row[2]] = [row[2], row[3]]
        return player

times = 150
class the_draft:
    def __init__(self, master):
        self.master = master
        self.master.focus()
        self.turn = 0
        self.player_search = ''
#       self.timer = 0

#        self.timer_label = Label(master, text='', width=10)
#        self.timer_label.grid(row=0, column=7, sticky=E)
        self.listbox = Listbox(master)
        self.listbox.bind('<Double-Button-1>', self.entry_insert)
        self.listbox.bind('<Return>', self.entry_insert)
        for player in players:
            self.listbox.insert(END, player)
        self.listbox.grid(row=3)

##        self.draft_table_var = StringVar()
##        self.draft_table_var.set(self.table())
##        self.draft_table = Label(master, textvariable=self.draft_table_var)
##        self.draft_table.grid(row=3, column=5, stick=W)
        
        self.player_label_var = StringVar()
        self.player_label_var.set(self.drafted())
        self.player_label = Label(master, textvariable=self.player_label_var)
        self.player_label.grid(row=4)

        self.label = Label(master, text='2017 Fantasy Draft')
        self.label.grid(row=0, column=5, sticky=N)

        self.choose_player_label = Label(master, text='Choose your player')
        self.choose_player_label.grid(row=1, sticky=W)

        self.team_label_var = StringVar()
        self.team_label_var.set(draft_order[self.turn])
        self.team_label = Label(master, textvariable=self.team_label_var)
        self.team_label.grid(row = 1, column = 5, sticky=N)

        self.player = StringVar()
        self.player_entry = Entry(master, textvariable=self.player)
        self.player_entry.grid(row=2)
        self.player_entry.bind('<Tab>', self.do_nothing)
        self.player_entry.bind('<BackSpace>', self.edit_search)
        self.player_entry.bind('<Return>',self.add_player)
        self.player_entry.bind('<Key>', self.search_players)
        self.player_entry.focus()
#        self.countdown(150)

#    def countdown(self, time=times):
#        if time >= 0:
#            self.m = time / 60
#            self.s = time % 60
#            self.timer_label.configure(text='%d:%d' % (self.m, self.s))
#            times = time - 1
#            root.after(1000, self.countdown)
#        else:
#            self.timer_label.configure(text='time\'s up!')


    def do_nothing(self, master):
        #prevents a tab search error by making tab call to this instead of <Key>
        pass

    def search_players(self, master=0):
        self.listbox.delete(0, END)
        try:
            if master.char.isalpha() == True or master.char.isspace() == True:
                self.player_search += master.char.lower()
        except:
            pass
        for player in players:
            if self.player_search in player.lower():
                self.listbox.insert(END, player)

    def edit_search(self, master):
        self.player_search = self.player_search[:-1]
        self.search_players()

    def entry_insert(self, master):
        self.player_entry.delete(0, END)
        self.player_entry.insert(0, self.listbox.get(self.listbox.curselection()))
        self.player_entry.focus()

    def add_player(self, master):
        if self.player.get() != '':
            teams[draft_order[self.turn]].append(self.player.get())
            try:
                del players[self.player.get()]
            except:
                pass
            self.player_entry.delete(0, END)
            self.turn += 1
            self.listbox.delete(0, END)
            self.player_search = ''
            for player in players:
                self.listbox.insert(END, player)
            if self.turn >= len(draft_order):
                self.turn = 0
                draft_order.reverse()

        self.team_label_var.set(draft_order[self.turn])
        self.player_label_var.set(self.drafted())
        self.draft_table_var.set(self.table())

    def drafted(self):
        self.team_players = ''
        for player in teams[draft_order[self.turn]]:
            self.team_players += player + '\n'
        return self.team_players

##    def table(self):
##        self.team_table = []
##        self.x = 0
##        self.y = 0
##        self.player_table = ''
##        for team in teams:
##            self.team_table.append(team)
##            self.player_table += '|%30s|' % team
##        self.player_table += '\n'
##        while self.x < len(teams[self.team_table[self.x]]):
##            self.all_players = []
##            while self.y < len(teams):
##                self.player_table +='|%30s|' % teams[self.team_table[self.y]][self.x]
##                self.y += 1
##            self.player_table += '\n'
##            self.x += 1
##            self.y = 0
##        return self.player_table
  
root = Tk()
teamers = makin_teams(root)
root.mainloop()

#store team dictionary: player, and owner:teamname
teams = teamers.add_team()[0]
owners = teamers.add_team()[1]
try:
    del teams['']
    del owners['']
except:
    pass

master = Tk()
orderin = draft_orderin(master)
master.mainloop()
draft_order = orderin.order_return()

players = playercsv()

root = Tk()
draftin = the_draft(root)
root.mainloop()

with open('2017draft.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    all_teams = []
    all_owners = []
    y = 0
    x = 0
    for team in teams:
        all_owners.append(owners[team])
    csv_writer.writerow(all_owners)
    for team in teams:
        all_teams.append(team)
    csv_writer.writerow(teams)
    while y < len(teams[all_teams[x]]):
        all_players = []
        while x < len(teams):
            all_players.append(teams[all_teams[x]][y])
            x += 1
        csv_writer.writerow(all_players)
        y += 1
        x = 0
