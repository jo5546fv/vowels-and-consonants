#variables and list
datastring = []
dataint = []
#I made the loop variable 
test = 1
#went pretty simple for the first part just straight input into variable
title = input('Enter a title for the data:\n')
print('You entered: %s\n' % title)

column1 = input('Enter the column 1 header:\n')
print('You entered: %s\n' % column1)

column2 = input('Enter the column 2 header:\n')
print('You entered: %s\n' % column2)
def data (name,point):
        print(name,point)
        print('Data string: %s' % name)
        print('Data integer: %s' % point)
        datastring.append(name)
        dataint.append(point)         
#this section needs to be done multiple times so while loop
while True:
    data1 = str(input('Enter a data point (-1 to stop input):\n'))
    real_data = data1.split(',')
    if data1 == '-1':
        break
    elif data1.count(',') >= 2:
        print('Error: Too many commas in input.\n')
    elif ',' not in data1:
        print('Error: No comma in string.\n')
    elif datalist[1].replace(' ','').isdigit() == False:
        print('Error: Comma not followed by an integer.\n')
    else:
         name = real_data[0]
         point = real_data[1]
         data(name,point) 
print(datastring)
print('%33s' % title)
print('%-20s|%23s' % (column1, column2))
for i in range(44):
    print('-',end='')
for i in range(len(datastring)):
    print('%-20s|%23d' % (datastring[i], dataint[i]))
