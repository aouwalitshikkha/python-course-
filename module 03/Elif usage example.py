"""
> 80        A+
> 70        A
> 60        A-
>50         B
>40         C
> 33        D
0-32        F
"""
number = int(input('Enter Number: '))

if number > 80:
    print('Grade is A+')
elif number > 70:
    print('Grade is A')
elif number > 60:
    print('Grade is A-')
elif number > 50:
    print('Grade is B')
elif number > 40:
    print('Grade is C')
elif number > 33:
    print('Grade is D')
else:
    print('Failtus')