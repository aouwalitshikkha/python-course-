car = {
    'brand': 'BMW',
    'model': '2010'
}
print('Past Model and Brand: ',car['model'], car.get('brand'))
car['brand'] ='Ford'
car.update({'model': 2022})
# add New Items
# car['Menufactured'] = 'USA'
car.update({'manufactured in': 'USA'})
print('New', car)

# car.pop('model')
# car.popitem()
# del car['brand']
car.clear()
print('Latest', car)