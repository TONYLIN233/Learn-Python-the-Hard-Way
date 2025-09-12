# 练习14.提示和传递
from sys import argv

# 检查是否有足够的参数
if len(argv) >= 2:
    script, username = argv
else:
    # 提供默认值或提示用户
    script = argv[0] if len(argv) > 0 else "script.py"
    username = input("请输入你的名字: ")

promt='>'

print(f"Hi {username}, I'm {script}.")
print("I'd like to ask you a few questions.")
print(f"Do you like me? {username}")
likes = input(promt)
print(f"where do you live in? {username}")
lives = input(promt)

print("what kind of computer do you have?")
computer = input(promt)


print(f"""
Alright, so you said {likes} about liking me.
You live in {lives} . Not sure where that is.
And you have a {computer} computer . Nice.
""")