# #练习17.更多文件操作
#不再使用打开，复制新建文件，再将源文件内容写入新文件的方式，直接使用shutul函数实现复制操作
import os
import shutil
import sys
#这套找文件的代码可以试试
def find_file(filename, search_path):
    """在指定路径下递归搜索文件"""
    for root, dirs, files in os.walk(search_path):
        if filename in files:
            return os.path.join(root, filename)
    return None

filename = "demo.txt"
# 创建文件
with open(filename, "w") as f:
    f.write("{line1}\n{line2}\n{line3}")
    # f.write("文件操作示例\n第一行\n第二行\n")
print(f"文件{filename}创建成功")
home_dir = os.path.dirname(os.path.abspath(__file__))
file_path  = os.path.join(home_dir, filename)

print(file_path)
# 在用户主目录下搜索文件
found_path  = find_file(filename, home_dir)
print(f"主目录：{home_dir}")

if found_path:
    print("找到文件:", found_path )
else:
    print("未找到文件")

from_file = found_path

to_dir = home_dir

new_file = "copydemo.txt"
# 组合目标路径：将目标目录和新文件名连接起来
destination_path = os.path.join(to_dir, new_file)
# 简单的修正：确保目标目录存在
os.makedirs(to_dir, exist_ok=True)  # 这行是关键！

print(f"目标地址：{destination_path}")
print(f"Copying from {from_file} to {destination_path}")

# 执行复制（并重命名）
shutil.copy2(from_file, destination_path)


print("复制完成！")

# import os
# import shutil
#
# # 1. 创建文件 - 在当前目录创建
# filename = "demo.txt"
# with open(filename, "w") as f:
#     f.write("{line1}\n{line2}\n{line3}")
# created_file_path = os.path.abspath(filename) # 获取当前文件的绝对路径
# print(f"文件已创建: {created_file_path}")
#
# # 2. 直接使用已知的源文件路径，不再需要 find_file 函数
# from_file = created_file_path
#
# # 3. 设置目标路径
# home_dir = os.path.expanduser("~")
# new_file_name = "copydemo.txt"
# destination_path = os.path.join(home_dir, new_file_name)
#
# # 4. 执行复制
# print(f"正在复制: {from_file} -> {destination_path}")
# shutil.copy2(from_file, destination_path) # 使用 copy2
# print("复制操作完成。请检查目标路径。")
