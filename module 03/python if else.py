"""
Messi is the footballer of Argentina. He is 36 years old.
"""

name = input("Enter the name: ")
profession = input('enter profession: ')
country = input('Enter country name: ')
birth_year = input('Enter birth year: ')
gender = input('enter m/f: ')

age = 2022 - int(birth_year)
if gender == 'm':
    pronoun = 'He'
else:
    pronoun = 'She'

text = f'{name} is the {profession} of {country}. {pronoun} is {age} years old.'

print(text)