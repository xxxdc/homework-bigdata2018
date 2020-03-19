from matrix_defination import Matrix

if __name__=='__main__':
    #t0=Matrix(-1,4,[5,4,6,9])
    #print(t0.array())

    t=Matrix(1,4,[5,4,6,9])
    print('t的矩阵：',t.array())
    print('t改变形状:',t.reshape(2,2.5))

    t1=Matrix(2,2,[4,5,6,7])
    t2=Matrix(2,3,[1,2,3,4,5,6])
    t3=Matrix(2,2,[1,0,9,8])
    print('t1的矩阵：', t1.array())
    print('t2的矩阵：', t2.array())
    print('t3的矩阵：', t3.array())
    print('t2改变形状：',t2.reshape(3,2).array())

    print('t1乘t2：',t1.mul(t2).array())
    print('t1加t2：',t1.add(t2))
    print('t1加t3：',t1.add(t3).array())
    print('t1减t3：',t1.sub(t3).array())
    print('t1的转置：',t1.T().array())
