# 1--20
# 2--19
# 3 -- 18
# number = 1
# while number < 21:
#     print(number,(21-number), sep='----')
#     number += 1

x = 1
y = 20

while x <= 20 and y >= 1:
    print(x, y, sep='----', end = ', ')
    x += 1
    y -= 1
