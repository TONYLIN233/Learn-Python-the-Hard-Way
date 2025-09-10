cars = 100
#车内空间可乘坐4人
#space_in_a_car = 4.0
space_in_a_car = 4

drivers = 30
#乘客数量
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
#汽车总承载量
carpool_capacity = drivers * space_in_a_car

average_passengers = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers, "in each car.")
print(f"We need to put about {average_passengers} in each car.")