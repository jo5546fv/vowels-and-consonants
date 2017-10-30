def vowel_check(string):
    '''check for vowels'''
    vowels = ['a','e','i','o','u']
    x = 0
    for i in string.lower():
        if i in vowels:
            x += 1
    return x
    
def consonant(string):
    '''check for consonants'''
    consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','u','v','w','x','y','z']
    x = 0
    for i in string.lower():
        if i in consonants:
            x += 1    
    return x
    
if __name__ == '__main__':
    text = input('Type a string in:\n')
    
print('Here are the consonants: %d' % consonant(text))
print('Here are the vowels: %d' % vowel_check(text))

