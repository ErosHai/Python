import os

# 定义旧文件名和新文件名
old_name = "old_file.txt"
new_name = "new_file.txt"

# 重命名文件
os.rename(old_name, new_name)
print(f"文件已从 {old_name} 重命名为 {new_name}")