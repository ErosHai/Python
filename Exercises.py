# 读写文件
with open('./file.txt','r+',encoding='utf-8') as f:
    print(f.read())


# 字典
car = {'name':'BMW','model':'X5','price': 80000}

print(len(car))
print(car['price'])