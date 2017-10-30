def vowel_check(string):
    vowels = ['a','e','i','o','u']
    x = 0
    for i in string:
        if i in vowels:
            x += 1

    return x
print(vowel_check('hello world'))
