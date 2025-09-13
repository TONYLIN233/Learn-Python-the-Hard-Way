# 习题 30: Else 和 If
people = 30
cars = 40
buses = 15
#车的数量比人的数量多的时候
if cars > people:
#打印我们应该去坐车
    print("We should take the cars.")
#车比人的数量少的时候
elif cars<people:
#我们不应该去坐车
    print("We should not take the cars.")
#其他情况我们不能决定
else:
    print("We can't decide.")

#公交比车子多的时候
if buses > cars:
#打印太多公交了
    print("That's too many buses.")
#公交比车子少的时候
elif buses < cars:
#打印也许我们应该去坐公交
    print("Maybe we could take the buses.")
#剩余情况
else:
#我们依然无法决定
    print("We still can't decide.")
#人比公交多的时候
if people > buses:
#打印我们就做公交
    print("Aright , let's just take the buses.")
#剩余情况
else:
    #让我们呆在家里吧
    print("Fine ,let's stay home then.")