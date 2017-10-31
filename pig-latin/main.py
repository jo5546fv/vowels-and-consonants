
sentence = input('Enter your sentence without any special charecters:\n').split()

pig_latin = ''
#Wont work with special charecters
for i in sentence:
    pig_latin = pig_latin + i[1:]+ i[0]+'ay '
    
print(pig_latin)
