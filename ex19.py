#习题19. 函数和变量
def cheese_and_crackers(cheese_count=None, boxes_of_crackers=None):
    print(f"You have {cheese_count} cheeses_count.")
    print(f"You have{boxes_of_crackers} boxes_of_crackers.")
    print("Man that's enough for a party.")
    print("Get a blanket.\n")

print("we can just give the function numbers directly:")
cheese_and_crackers(20,30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10+20,5+6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+100)

#增加对input的使用方法
print("We can even do input inside too:")
amount_of_cheese =input("请输入cheese_count数量：")
amount_of_crackers = input("请输入boxes_of_crackers数量：")
cheese_and_crackers(amount_of_cheese, amount_of_crackers)