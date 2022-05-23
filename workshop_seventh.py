word = input('Enter a word: ')
suffix = input('Enter a suffix: ')

if(word[-len(suffix)::] == suffix):
    print('Entered word has the suffix.')
else:
    print('Doesnt contain suffix.')
