# 习题 33: While 循环
i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")

    numbers.append(i)

    i = i + 1
    print("Numbers after adding i:", numbers)
    print(f"At the bottom i is {i}")

print("The numbers:")

for number in numbers:
    print(number)

