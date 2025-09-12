#判断这是不是一个三角形
import numpy as np
a= input("请输入a：")
b= input("请输入b：")
c= input("请输入c：")
# 将字符串转换为整数（如果期望输入整数）
try:
    a_num = int(a)
    b_num = int(b)
    c_num = int(c)
except ValueError:
    # 如果转换失败（例如输入了非数字字符），可以处理错误或退出
    print("输入错误，请输入数字！")
    exit(1)  # 非正常退出程序
arr =np.asarray([a,b,c])
sorted_arr = np.sort(arr)
# print(sorted_arr)
if sorted_arr[0] + sorted_arr[1] > sorted_arr[2] and sorted_arr[2] >0 and  sorted_arr[1] > 0 and sorted_arr[0] > 0 :
    print("这是一个三角形")
else:
    print("这不是一个三角形")