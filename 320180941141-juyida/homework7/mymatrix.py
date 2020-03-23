from numpy import array as matrix, arange
import numpy as np
print("初始化第一个矩阵")
long=int(input("请输入矩阵的长"))
wide=int(input("请输入矩阵的宽"))
space=long*wide
choose1=int(input("请做出选择：\n1:矩阵由代码默认生成\n2:自行输入\n"))
if choose1==1:#确定矩阵大小并赋值
    a = arange(space).reshape(long,wide)
    print(a)

else:
    a = np.empty([long,wide], dtype=int)#确定矩阵类型
    for i in range(long):#通过循环自行赋值
        for j in range(wide):
            a[i][j]=int(input())
            print(a)

print("初始化第二个矩阵")#和上一段一样
long=int(input("请输入矩阵的长"))
wide=int(input("请输入矩阵的宽"))
space=long*wide
choose1=int(input("请做出选择：\n1:矩阵由代码默认生成\n2:自行输入\n"))
if choose1==1:
    b = arange(space).reshape(long,wide)
    print(b)

else:
    b = np.empty([long,wide], dtype=int)
    for i in range(long):
        for j in range(wide):
            b[i][j]=int(input())
            print(b)

print("请选择矩阵间的运算关系")


choose2=int(input("1:加法运算\n2:减法运算\n3:数乘运算\n4:点乘运算\n5:矩阵求逆\n6:矩阵转置"))
print("5,6默认为第一个矩阵，5要求矩阵为方阵")
if choose2==1:
    print(a+b)
if choose2==2:
    print(a-b)
if choose2==3:
    a3=int(input("请输入数乘的数字（数乘的对象默认为第一个）"))
    print(a3*a)
if choose2==4:
    print(a*b)
if choose2==5:
    print(np.transpose([a]))#只能对方阵进行转置
if choose2==6:
    print(np.transpose(a))
    print("默认为第一个")

if __name__ =='__main__':
    import doctest
    doctest.testmod()