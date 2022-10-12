ch = 'y'
names = []
while ch.lower() == 'y':
    name = input('What is your name: ')
    names.append(name)
    ch = input('Do you want to continue(y/n)')

print(names)