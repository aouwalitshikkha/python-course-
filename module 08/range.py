# x = range(6)
# for y in x:
#     print(y)

numbers = range(10, 61, 10)
sum = 0
for number in numbers:
    sum += number

print('The Grand total is:', sum )

# range(6) --- 0,1,2,3,4,5 ---- range(end)
# range(1,6) --- 1,2,3,4,5 ---- range(start, end)
# range(1,6,2) --- 1,3,5 -- range(start, end, step)
