# gender = input('Enter M/F: ')
#
# if gender.lower() == 'm':
#     gender = 'male'
#     pronoun = 'He'
#     relative_pronoun = 'his'
# else:
#     gender = 'Female'
#     pronoun = 'She'
#     relative_pronoun = 'her'
#
# print(gender,pronoun, relative_pronoun)
#
# i = 1
# while i < 20:
#     print(i)
#     i += 2
# #     i = i+2

# person = ['Abdul Aouwal', 32, True]
# person[-1] = False
# if person[-1] == True:
#     marital_status = 'Married'
# else:
#     marital_status = 'Single'
# templates = f'This is {person[0]}. I am {person[1]} years old.  I am {marital_status}'
# print(templates)

fruit_list = [ "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruit_list[3:])
if 'apple' in fruit_list:
    print('He eats Apple')
else:
    print('He doesn\'t eat apple')