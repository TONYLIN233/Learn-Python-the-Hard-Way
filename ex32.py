# 习题 32: 循环和列表

hairs = ['brown' ,'blond' ,'red']

eyes = ['brown' ,'blue','green']

weights = [1,2,3,4]



the_count = [1,2,3,4,5]

fruits = ['apples','oranges','pears','apricots']

change = [1,'pennies',2,'dimes',3,'quarters']

#this first kind of for-loop goes through a list
for number in the_count :
    print(f"This is coount {number}")

#same as above
for fruit in fruits:
    print(f"A fruit of type:{fruit}")

#also we can go through mixed lists too
for i in change :
    print(f"I got {i}")

elements = []


#now we can print them out too
for i in range(0,6):
    print(f"Adding {i} to the list.")

    elements.append(i)

#now we can print them out too
for i in elements:
    print(f"Element was:{i}")



