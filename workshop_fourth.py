numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numFound = False

username = input('Enter your username: ')


for num in numbers:
    if str(num) in username:
        print('Username should not contain any number.')
        numFound = True
        break
    else:
        continue

if numFound == False:
    print(f'Welcome! {username}.')
