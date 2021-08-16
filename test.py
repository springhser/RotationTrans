'''
Descripttion: 
version: 
Author: springhser
Date: 2021-08-13 11:46:37
LastEditors: springhser
LastEditTime: 2021-08-13 14:57:47
'''
from scipy.spatial.transform import Rotation as R
import numpy as np

r = R.from_euler("xyz", [0,-45,0], degrees=True)
print(r.as_matrix())
tm = r.as_matrix()
# print(type(tm))

I = 0
J = 45
K = 0

Rx = R.from_euler("x",[I], degrees=True).as_matrix()
Ry = R.from_euler("y",[J], degrees=True).as_matrix()
Rz = R.from_euler("z",[K], degrees=True).as_matrix()

print(Rx)
print(Ry)
print(Rz)

p = np.array([1,0,0])
p1 = tm.dot(p)

print(p1)

# translation_matrix = np.array()