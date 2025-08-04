# 读写文件
with open('./file.txt','r+',encoding='utf-8') as f:
    print(f.read())


# 字典
cars = {'name':'BMW','model':'X5','price': 80000}

print(len(cars))
print(cars['price'])

for key, value, in cars.items():
    print(f'{key} : {value}')

