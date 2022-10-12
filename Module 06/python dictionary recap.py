bio = {
    'name': 'Aouwal',
    'age':'32 years',
    'home town': 'Chittagong'
}

# Access
# print(bio['name'], bio.get('age'))
print(bio)
# Change and add
bio['full name'] = 'M. A. Aouwal'
bio.update({'age': '23 years'})
print(bio)

# Remove Items
bio.pop('name')
bio.popitem()
print(bio)

# accessing keys and values
print(bio.keys())
print(bio.values())

# membership Operators
if 'age' in bio.keys():
    print('Your age is', bio['age'])

print(bio.items())
