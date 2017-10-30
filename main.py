def vowel_check(string):
    vowels = ['a','e','i','o','u']
    x = 0
    
    for i in string:
        if i in vowels:
            x += 1
    return x
    print('Here are the vowels %d' % x)
def consonant(string):
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','u','v','w','x','y','z']
    x = 0
    
    for i in string:
        if i in consonants:
            x += 1    
    
    return x
    


if __name__ == '__main__':
    text = input('Type a string in:\n')
    consonant(text)
    vowel_check(text)
print('Here are the consonants: %d' % consonant(text))
print('Here are the vowels: %d' % vowel_check(text))

