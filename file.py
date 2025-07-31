# 读取文件
with open('./file.txt', 'r', encoding='utf-8') as f:
    # content = f.read()
    # print(content)
    #
    # print(f.readline())
    # print(f.readlines())

    lines = f.readlines()
    for line in lines:
        print(f'- {line}')

