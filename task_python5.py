# data = {'one': 1, 'two': 2}
# x = iter(data.items())
# print(x)
# y = next(x)
# print(y)
# z = next(iter(y))
# print(z)
# a = 8
# b = 10
# print(f'{a=}\t{b=}')
data = {2, 3, 4, 10, 11, 8, 9}
# res = []
# for i in data:
#     if i % 2 == 0:
#         res.append(i) 
# print(res)
#res =[i for i in data if i % 3  == 0]
data = {2, 3, 4, 10, 11, 8, 9}
res1 = ( i for i in data if i > 4)
print(res1)
