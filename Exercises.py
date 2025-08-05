# 读写文件
with open('./file.txt','r+',encoding='utf-8') as f:
    print(f.read())


# 字典
cars = {'name':'BMW','model':'X5','price': 800000}

print(len(cars))
print(cars['price'])

for key, value, in cars.items():
    print(f'{key} : {value}')


# 列表去重后排序，找到第二大的数
arrs = [13,8,4,8,6,10,13]

Unique_lists = sorted(set(arrs))

print(Unique_lists)
print(Unique_lists[-2])
