# 习题 28: 布尔表达式练习

#答对了18/20题，准确率90%
#我的答案True
print(True and True)

print(False and True)#f

print(1==1 and 2==1 )#f

print("test" == "test")#t

print(1 ==1 or 2 != 1) #t

print(True and 1 == 1)#t


#False and False结果是 False
print(False and 0 !=0) #t

print(True or 1 ==1) #t

print("test" == "testing") #f

print(1 !=0 and 2 ==1)#f

print("test" != "testing") #t

print("test" ==1) #f

print(not(True and False))#t

print(not(1 == 1 and 0!=1))#f

print(not(10 == 1 or 1000 ==1000))#f

print(not(1 != 10 or 3 ==4))#f

print(not("testing" == "testing"  and "zed" == "cool guy"))#t



# True and True最终结果是 True
print(1==1 and not("testing" ==1 or 1==0))#f

print("chunky" == "bacon" and not(3 == 4 or 3==3))#f

print(3==3 and not("testing" == "testing" or "python" == "fun"))#f