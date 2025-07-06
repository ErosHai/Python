slang_dir = {
    'yyds': '永远的神 (yǒngyuǎn de shén; yyds) 的意思是“永恒的上帝”并描述杰出的人或事。 它类似于英语中的 GOAT (Greatest of All Time)。 这句话经常被粉丝用来赞美他们的偶像或简单地描述他们喜欢的东西。',
    'nsdd': '你说得对 (nǐ shuō dé duì; nsdd) 的意思是“你说的是对的”，通常用于赞同或赞同某人所说的话',
    'srds': '虽然但是（suīrán dànshì；srds），翻译为“尽管如此”或“尽管如此”，用在句首，表示说话者的观点发生了转变。',
}

slang_dir['xswl'] = '“笑死我了”（xiào sǐ wǒ le; xswl）字面意思是“笑死”，说话者用它来回应一些有趣的事情，类似于英语中的LOL。'

search_key = input('input your search: ')

if search_key in slang_dir:
    print('This slang means: ',slang_dir[search_key])
else :
    print('SORRY , NOT FOUND Total: ' ,str(len(slang_dir))+ ' item')


#  dir 循环
people_dir ={
    'zhang san':18,
    'li si':32,
    'wang wu':26
}

for name, age in people_dir.items():
    if age <= 30:
        print(name)

# 1~100求和
total = 0
for i in range(1,101):
    total = total + i
print(total)

print(range(5))

# dir 格式化字符串两种写法
gpa_dir = {
    'zhang san':3.154,
    'li si':3.266,
    'wang wu':3.566,
}

for name, gpa in gpa_dir.items():
    print("name: {0}, gpa: {1}".format(name, gpa))
    print(f"name: {name}, gpa: {gpa:.2f}")