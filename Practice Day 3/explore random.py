import random
number = [10,20,30,100,50,652,62,265,32,41,97,70]
random_number = random.choice(number)
# print(random_number)

user_name = input('Enter your name: ')
sentences = [
    f'This is {user_name}',
    f'My Name is {user_name}',
    f'Hello, I am {user_name}',
    f'Hi, I am Abdul {user_name}'
]
print(random.choice(sentences))