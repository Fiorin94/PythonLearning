name = input('type hyour name: ' )
age = input('Type your age: ')

if name and age:
    print( f'Your name is {name}')
    print( f'Your name reversed is {name[::-1]}')
    if ' ' in name:
        print('Your name has spaces')
    else:
        print('Your name has no spaces')
    print(f'Your name has {len(name)} letters')
    print(f'The first letter of your name is {name[0]}')
    print(f'The last letter of your name is {name[-1]}')
else:
    print("Desculpe mas você deixou campos vazios")