import numpy as np
#############################################
x = np.arange(5)
# [0 1 2 3 4]
x[0]
# 0
#############################################
x = np.arange(12).reshape(3,4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
x[0,2]
# 2
#############################################
x = np.arange(6)
# [0 1 2 3 4 5]        

x = np.delete(x, [0,1])
# [2 3 4 5]
#############################################
x = np.arange(16).reshape(4,4) #axis = 0 row-satir, axis=1 column sutun
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]

x = np.delete(x, 1, axis=0)
# [[ 0  1  2  3]
#  [ 8  9 10 11]
#  [12 13 14 15]]

x = np.delete(x, [0,1], axis=1)
# [[ 2  3]
#  [10 11]
#  [14 15]]
#############################################
x = np.arange(5)
# [0 1 2 3 4]

x = np.append(x, 100)
# [  0   1   2   3   4 100]

x = np.append(x, [23, 45])
# [  0   1   2   3   4 100  23  45]
#############################################
x = np.arange(9).reshape(3,3)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

x = np.append(x, [[56, 78, 65]], axis=0)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [56 78 65]]

x = np.append(x, [[21], [22], [23], [24]], axis=1)
# [[ 0  1  2 21]
#  [ 3  4  5 22]
#  [ 6  7  8 23]
#  [56 78 65 24]]
#############################################
x = np.arange(5)
# [0 1 2 3 4]

x = np.insert(x, 3, [90, 100])
# [  0   1   2  90 100   3   4]
#############################################
x = np.arange(9).reshape(3,3)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

x = np.insert(x, 1, [10, 20, 30], axis=0)
# [[ 0  1  2]
#  [10 20 30]
#  [ 3  4  5]
#  [ 6  7  8]]

x = np.insert(x, 2, [50, 60, 70, 80], axis=1)
# [[ 0  1 50  2]
#  [10 20 60 30]
#  [ 3  4 70  5]
#  [ 6  7 80  8]]
#############################################
x = np.arange(3)
# [0 1 2]

y = np.arange(9).reshape(3,3)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

z = np.vstack((x,y))#dikey
# [[0 1 2]
#  [0 1 2]
#  [3 4 5]
#  [6 7 8]]

t = np.hstack((x,y.reshape(9,)))#yatay
# [0 1 2 0 1 2 3 4 5 6 7 8]
#############################################