# 习题 10: 那是什么？
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
#\t 水平制表符
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

#"abcd\b"-> abc   \b 退格符
print("abcd\b")
#'It\'s me'-> It's me    \' 单引号 (')
print('It\'s me')
#"He said, \"Hi\""-> He said, "Hi"     \"	双引号 (")
print("He said, \"Hi\"")
#"Hello\rWorld"-> World       \r 回车符
print("Hello\rWorld")


#无需转 译原始字符串（Raw String）
# 普通字符串（麻烦，需要转义）
path = "C:\\Users\\Name\\Documents"
# 原始字符串（方便！）
path = r"C:\Users\Name\Documents"
print(path) # 输出: C:\Users\Name\Documents

#无需转 加三引号字符串
path = "C:\\Users\\Name\\Documents"
print("C:\\Users\\Name\\Documents","""C:\\Users\\Name\\Documents""")