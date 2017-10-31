def table(title,column1,column2):
    #made a couple empty lists
    datastring = []
    dataint = []
    
    while True:
        data = input('Enter a data point (-1 to stop input):\n')
        datalist = data.split(',')
        #checking for errors and -1
        if data == '-1':
            print()
            break
        elif ',' not in data:
            print('Error: No comma in string.\n')
        elif data.count(',') >= 2:
            print('Error: Too many commas in input.\n')
        elif datalist[1].replace(' ','').isdigit() == False:
            print('Error: Comma not followed by an integer.\n')
        else:
            print('Data string: %s' % datalist[0])
            print('Data integer: %s\n' % datalist[1].replace(' ',''))
            datastring.append(datalist[0])
            dataint.append(int(datalist[1]))

    #print the formated table, and histogram
    #python is fun
    print('%33s' % title)
    print('%-20s|%23s' % (column1, column2))
    for i in range(44):
        print('-',end='')
    print()
    for i in range(len(datastring)):
        print('%-20s|%23d' % (datastring[i], dataint[i]))
    else:
        print()
    for i in range(len(datastring)):
        print('%20s' % datastring[i],end=' ')
        for x in range(dataint[i]):
            print('*', end='')
        else:
            print()

if __name__ == '__main__':
    header = input('Enter a title for the data:\n')
    print('You entered: %s\n' % header)

    column1 = input('Enter the column 1 header:\n')
    print('You entered: %s\n' % column1)

    column2 = input('Enter the column 2 header:\n')
    print('You entered: %s\n' % column2)

    table(header, column1, column2)
