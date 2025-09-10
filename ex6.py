# 练习6.字符串和文本
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
print(x)
print(y)

print("I said %r." % x)
print("I also said %r." % y)

#这个用法之前没有用过
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)
#原因写在m变量里，增加了换行符
w = "This is the left side of ..."
e = "a string with a right side ."
m = "我觉得两个字符串拼接本身就是组合成一个新的字符串，所以长度会不停增加"
print(w + e  +'\n' +m+'\n')
#一种新的写法python3 常用，直接在f中完成换行操作
print(f"""
新的表达方式{w}{e}
{m}""")

