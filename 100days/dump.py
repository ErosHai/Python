import json

my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}

# dumps 字典转化成JSON格式
data = json.dumps(my_dict,indent = 2,ensure_ascii=False,sort_keys=True)
print(data)

# dump 转化为JSON格式并写入到文件
with open('data.json','w',encoding='utf-8') as f:
    json.dump(my_dict, f)
f.close()