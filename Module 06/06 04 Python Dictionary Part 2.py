mobile = {'name':'Xiaomi Note 10',
          'brand': 'Xiaomi',
          'ram': '4GB',
          'rom': '64GB'
          }

# print(mobile['ram'])
# print(mobile.get('rom'))

print('Previous:',mobile)
mobile['rom'] = '32 GB'
# mobile['camera'] = '2mp'
mobile.update({'camera':'10mp'})
print('After Update:',mobile)



