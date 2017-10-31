#commits
full_name = input('enter your full name\n')
name = full_name.split()
for i in range(len(name)):
    print('%s.' % name[i][0], end='')
