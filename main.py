def vowel_check(string):
    vowels = ['a','e','i','o','u']
    x = 0
    for i in string:
        if i in vowels:
            x += 1

    return x

def constent(string):
    contents = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','u','v','w','x','y','z']
    x = 0
    for i in string:
        if i in contents:
            x += 1    
    print('Here are the constinets %d' % x)
string = input('Type a string in:\n')
constent(string)
vowel_check(string)


if __name__ == '__main__':
    text = input('Enter your sentence\n')
