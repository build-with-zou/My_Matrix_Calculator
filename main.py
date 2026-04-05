# Test code for IEEE course final project
# Fan Cheng, 2024

import minimatrix as mm


def test_main():
    mat = mm.Matrix(data = [[1,0,0],[1,0,0],[0,0,9]])
    mat1 = mm.Matrix(dim = (3,3),init_value= 1)
    print(mat.shape())
    print()
    print(mat.reshape((9,1)))
    print()
    print(mat.dot(mat))
    print()
    print(mat.dot(mat1))
    print()
    print(mat.T())
    print()
    print(mat.sum(axis=1))
    print()
    print(mat.sum(axis=0))
    print()
    print(mat.copy())
    print()
    print(mat.Kronecker_product(mat))
    print()
    mat[:,1:] = [[2,2],[1,3],[2,3]]
    print(mat.data)
    print(mat.__pow__(2))
    print(mat.__add__(mat))
    print(mat.__sub__(mat))
    print(mat.__mul__(mat))
    print(mat.__len__())
    print(mat)
    print(mat.det())
    # print(mat.inverse())
    print(mat.rank())
    print(mm.I(4))
    print(mm.narray(dim = (2,3),init_value= 4))
    print(mm.arange(2,7,2))
    print(mm.zeros(dim = (2,4)))
    print(mm.zeros_like(mat))
    print(mm.ones(dim = (2,4)))
    print(mm.ones_like(mat))
    print(mm.nrandom(dim = (3,4)))
    print(mm.nrandom_like(mat))
    print(mm.concatenate((mat,mat1)))
    print(mm.concatenate((mat,mat1),axis= 1))
    def func(x):
        return x**2
    F = mm.vectorize(func)
    print(F(mat).data)
    print(mat[1:,2:])
    mat[1:,2:] = [[1],[2]]
    print(mat[1:,2:])


# def other():
#     # 2: Test arrange
#     m24 = mm.arange(0,24,1)
#     print (m24.data)
#     print (m24.reshape((3,8)))
#     print()
#     print (m24.reshape([24,1]))
#     print()
#     print (m24.reshape((4,6)))
#     print()
#     # #3: Test zeros
#     print(mm.zeros((3,3)))
#     print()
#     print(mm.zeros_like(m24))
#     print()
#     # #4: Test ones
#     print(mm.ones((3,3)))
#     print()
#     print(mm.ones_like(m24))
#     print()
#     # #5: Test randoms
#     print(mm.nrandom((3,3)).data)
#     print()
#     print(mm.nrandom_like(m24).data)
#     print()

#     # another problem
#     m = 1000
#     n = 100
#     X = mm.nrandom((m,n))
#     X_ = X.copy()
#     w = mm.nrandom((n,1))
#     w_ = w.copy()
#     e = mm.nrandom((1000, 1))
#     a = sum(e.data[i][0] for i in range(1000))/1000
#     #实现零均值的方法！
#     for i in range(1000):
#         e.data[i][0] -= a
#     Y_ = X.dot(w)
#     Y = Y_.__add__(e)
#     X_T_X = (X.T()).dot(X)
#     W =(((X_T_X.inverse()).dot(X.T()))).dot(Y)
#     print(w.data)
#     print()
#     print(W.data)
#     res = W - w
#     #计算误差：
#     err = sum(res.data[i][0] for i in range(100)) / 100
#     print(err)

test_main()
# other()