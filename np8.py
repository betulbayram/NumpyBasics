import numpy as np

x = np.array([2,5,3,6,9, 3, 6, 5 ,0])
y = np.array([6,1,8,7,3])

z = np.intersect1d(x, y)
# [3 6]

print(type(z))
# <class 'numpy.ndarray'>

print(np.setdiff1d(x,y))
# [0 2 5 9]

print(np.setdiff1d(y,x))
# [1 7 8]

print(np.union1d(x,y))
# [0 1 2 3 5 6 7 8 9]

print(np.in1d(x,y))
# [False False  True  True False  True  True False False]

print(np.unique(x))
# [0 2 3 5 6 9]

x = np.random.randint(1,10, size=(10,))
# [8 1 4 8 1 9 4 9 7 5]

print(np.sort(x))
# [1 1 4 4 5 7 8 8 9 9]

print(x)
# [8 1 4 8 1 9 4 9 7 5]

y = np.random.randint(1,10, size=(10,))
# [2 4 5 6 9 2 7 9 6 2]

y.sort()

print(y)
# [2 2 2 4 5 6 6 7 9 9]

