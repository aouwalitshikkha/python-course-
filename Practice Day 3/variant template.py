import random
'''
1. List -- Name, age
2. The name of this celebrity is Omuk, He is 25 years old
'''
celebrity_name_list = ['Ananta Khalil','Piyaj','Razzak','Jafar khan', 'Rakib Khan', 'Solomon Khan', 'Bappa Raj', 'Alamzir']
celebrity_age_list = [40,38,38,45, 60,45,32,60]
i = 0
while i < len(celebrity_name_list):
    celebrity_name = celebrity_name_list[i]
    celebrity_age = celebrity_age_list[i]

    sentence_one_list = [
        f'The name of this celebrity is {celebrity_name}.',
        f'Let Introduce the celebrity {celebrity_name}.',
        f'This celebrity is known as {celebrity_name}.',
        f'{celebrity_name} is one of the popular celebrity in internet.',
    ]
    sentence_two_list = [
        f'He is {celebrity_age} years old.',
        f'His age is {celebrity_age} years.',
        f'This celebrity\'s age is {celebrity_age} years.',
        f'{celebrity_age} years has been passed after the birth of this celebrity.',
    ]
    sentence_one = random.choice(sentence_one_list)
    sentence_two = random.choice(sentence_two_list)
    print(sentence_one, sentence_two)

    i += 1

