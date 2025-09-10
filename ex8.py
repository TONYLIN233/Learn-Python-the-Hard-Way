#练习8.打印, 打印
formatter = "%r %r %r %r"

print(formatter % (1, 2, 3, 4))
print(formatter % ("one", "two", "three", "four"))
print(formatter % (True, False, False, True))
#什么可以用formatter，代替%r，不存在重复或者识别的问题吗
print(formatter % (formatter, formatter, formatter, formatter))
print(formatter % ("I had this thing.",
                   "That you could type up right.",
                   "But it didn't work.",
                   "So I said goodnight."))
#python3.6以上的写法
a, b, c, d = 1, "two", [3], {"four": 4}
print(f"{a!r} {b!r} {c!r} {d!r}")