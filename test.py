'''
Descripttion: 
version: 
Author: springhser
Date: 2021-08-13 11:46:37
LastEditors: springhser
LastEditTime: 2021-08-18 15:50:36
'''
from scipy.spatial.transform import Rotation as R
import numpy as np


def reshapeMatrix(mat):
    E = np.eye(4,4)
    # print(E)
    for i in range(0,3):
        for j in range(0,3):
            t = mat[0][i][j]
            E[i][j] = t

    # print(E)
    return E


def getTranslateMatrix(x, y, z):
    E = np.eye(4,4)
    E[0][3] = x
    E[1][3] = y
    E[2][3] = z
    return E

# r = R.from_euler("xyz", [0,-45,0], degrees=True)
# print(r.as_matrix())
# tm = r.as_matrix()
# print(type(tm))



if __name__ == "__main__":
    I = 0
    J = 45
    K = 0
    X = 50
    Y = -50
    Z = 0
    Rx = R.from_euler("x",[I], degrees=True).as_matrix()
    Ry = R.from_euler("y",[J], degrees=True).as_matrix()
    Rz = R.from_euler("z",[K], degrees=True).as_matrix()

    # print(Rx)
    # print(Ry)
    # print(Rz)
    # print(Rx.shape)

    Ry4 = reshapeMatrix(Ry)
    Rx4 = reshapeMatrix(Rx)
    Rz4 = reshapeMatrix(Rz)


    Tmat = getTranslateMatrix(X, Y, Z)

    print(Tmat)

    Mat = Tmat@Rz4@Ry4@Rx4

    print(Mat)

    
    p = np.array([1,0,0,1])

    Res = np.matmul(Mat, p)

    print(Res)