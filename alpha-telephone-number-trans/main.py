phone_letter = {
    'A':'2',
    'B':'2',
    'C':'2',
    'D':'3',
    'E':'3',
    'F':'3',
    'G':'4',
    'H':'4',
    'I':'4',
    'J':'5',
    'K':'5',
    'L':'5',
    'M':'6',
    'N':'6',
    'O':'6',
    'P':'7',
    'Q':'7',
    'R':'7',
    'S':'7',
    'T':'8',
    'U':'8',
    'V':'8',
    'W':'9',
    'X':'9',
    'Y':'9',
    'Z':'9'
}
#this will do the work
phone_number = input('enter a 10 digit phone number(XXX-XXX-XXXX)\n')
new_number = ''
for i in range(len(phone_number)):
    if phone_number[i].isdigit() == True:
        new_number = new_number + phone_number[i]
    elif phone_number[i] == '-':
        new_number = new_number + phone_number[i]
    else:
        new_number = new_number + phone_letter[phone_number[i]]

print(new_number)
