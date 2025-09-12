# 练习20.函数和文件
import os
import pathlib
from sys import argv
from ex17 import find_file
# script, input_file = argv
filename = "copydemo.txt"
#3.0以前
# home_dir = os.path.dirname(os.path.abspath(__file__))
#3.4以后
home_dir = pathlib.Path(__file__).parent.parent.resolve()
input_file = find_file(filename, home_dir)
def print_all(f):
    print(f.read())
def rewind(f):
    f.seek(0)
def print_a_line(line_count, f):
    print(line_count, f.readline())

current_life = open(input_file)

print("Fisrt let's print the whole life")
print_all(current_life)

print("Now let's rewind , kind of like a tape :)")
rewind(current_life)

print("Let's print three lines")
current_line =1
print_a_line(current_line, current_life)

current_line =current_line +1
print_a_line(current_line, current_life)

current_line =current_line +1
print_a_line(current_line, current_life)
