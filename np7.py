import numpy as np

x = np.linspace(1,21,11)
# [ 1.  3.  5.  7.  9. 11. 13. 15. 17. 19. 21.]

y = np.array([2, 4, 7])
# [2 4 7]

print(x[y])
# [ 5.  9. 15.]

x = np.arange(25).reshape(5,5)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]
#  [20 21 22 23 24]]

y = np.array([1,2])
# [1 2]

print(x[y, :])
# [[ 5  6  7  8  9]
#  [10 11 12 13 14]]

print(x[:,y])
# [[ 1  2]
#  [ 6  7]
#  [11 12]
#  [16 17]
#  [21 22]]

x = np.random.randint(10, size=10)
# [8 6 6 6 0 5 8 4 4 3]

y = np.random.randint(10, size=10)
# [3 4 4 3 6 2 8 7 2 7]

print(x>y)
# [ True  True  True  True False  True False False  True False]

print(type(x>y))
# <class 'numpy.ndarray'>

print((x>y).dtype)
# bool

print(np.all(x>y))
# False

print(np.any(x>y))
# True

x = np.linspace(1,21,11)
# [ 1.  3.  5.  7.  9. 11. 13. 15. 17. 19. 21.]

mask = (x % 3 == 0)
# [False  True False False  True False False  True False False  True]

print(type(mask))
# <class 'numpy.ndarray'>

print(x[mask])
# [ 3.  9. 15. 21.]

x[mask] = -3
# [ 1. -3.  5.  7. -3. 11. 13. -3. 17. 19. -3.]




