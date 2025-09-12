#练习15.读文件
from sys import argv

# 检查参数数量
if len(argv) < 2:
    print("错误：需要指定文件名")
    print(f"用法: python {argv[0]} 文件名")
    exit(1)

script, filename = argv[0], argv[1]

# 打开文件
try:
    txt = open(filename)
    print(f"成功打开文件: {filename}")

    # 读取并打印文件内容
    print("\n文件内容:")
    print(txt.read())

    # 关闭文件
    txt.close()

except FileNotFoundError:
    print(f"错误：找不到文件 {filename}")
    exit(1)
except Exception as e:
    print(f"读取文件时出错: {str(e)}")
    exit(1)


