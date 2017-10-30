sentence = input('Enter your sentence:\n').split()

pig_latin = ''

for i in sentence:
    pig_latin = pig_latin + i[1:]+ i[0]+'ay '
    
print(pig_latin)
