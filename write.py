# 写入文件
with open('./unknow.txt', 'r+', encoding='utf-8') as f:

    f.write('Hello \n')
    f.write('Sea \n')

    print(f)

    content = f.readlines()
    for line in content:
        print(line)