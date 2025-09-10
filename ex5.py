#练习5.更多的变量和打印
my_name = 'zed A. Shaw'
my_age = 35 # not a lie
my_height = 74
my_weight = 180
my_eye = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("let's talk about %s ." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." % (my_eye, my_hair))
print("His teeth are usually %s depending on her." % my_teeth)
#this line is tricky , try to get is exactly right
#my_age + my_height + my_weight 几个变量的加和
print("if I add %d, %d,and %d I get %d." % (my_age, my_height, my_weight , my_age + my_height + my_weight))