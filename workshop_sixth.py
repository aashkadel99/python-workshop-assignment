word = input('Enter a word: ')
prefix = input('Enter a prefix: ')

if(word[0:len(prefix)] == prefix):
    print('Entered word has the prefix.')
else:
    print('Doesnt contain prefix.')
