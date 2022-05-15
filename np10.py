import numpy as np

x = np.random.randint(1, 10, size=(8,))
# [6 6 1 9 9 7 6 7]

print(x.mean())
# 6.375

print(np.median(x))
# 6.5

print(x.std())
# 2.341874249399399

x = np.random.randint(1, 10, size=(1))
# [4]

y = np.random.randint(1, 10, size=(3,2))
# [[8 9]
#  [1 8]
#  [2 8]]

print(x + y)
# [[12 13]
#  [ 5 12]
#  [ 6 12]]
