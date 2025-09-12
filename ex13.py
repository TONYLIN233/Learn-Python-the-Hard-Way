# 练习13.参数, 解包, 变量
# from sys import argv
# PyCharm 是一个集成开发环境（IDE），它默认不会像命令行那样传递参数。你需要明确告诉它要传递哪些参数。
# script, first,second,third = argv
#
# print("The script is:", script)
# print("The first argument is:", first)
# print("The second argument is:", second)
# print("The third argument is:", third)
#

from sys import argv

# 检查是否有足够的参数
if len(argv) >= 4:
    script, first, second, third = argv
else:
    # 提供默认值或提示用户
    script = argv[0] if len(argv) > 0 else "script.py"
    first = input("请输入第一个参数: ")
    second = input("请输入第二个参数: ")
    third = input("请输入第三个参数: ")

print("The script is:", script)
print("The first argument is:", first)
print("The second argument is:", second)
print("The third argument is:", third)