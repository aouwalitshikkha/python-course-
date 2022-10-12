
# do you want to continue(y/n)
ch = 'y'
sum = 0
while ch.lower() == 'y':
    number = float(input('Enter any number: '))
    # sum = sum + number
    sum += number
    ch = input('Do you want to continue(y/n): ')
print('Sum of all number', sum)


