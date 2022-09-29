# name = input('Enter your Name: ')
# if name == '':
#     print('You don\'t enter anything')

number = int(input('Enter a positive Number: '))
while number < 0:
    number = int(input('Enter a positive Number: '))

print('Square root of', number,'is', number ** 0.5)


