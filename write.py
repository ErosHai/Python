# 写入文件 w模式会删除之前内容 a模式是原有内容后增加 r+是可读写的模式
with open('./unknow.txt', 'r+', encoding='utf-8') as f:
    content = f.readlines()
    for line in content:
        print(line)

    f.write('Hello \n')
    f.write('Sea \n')
