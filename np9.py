import numpy as np

x = np.random.randint(1, 10 , size=(5,))
# [3 3 6 4 7]

y = np.random.randint(1, 10 , size=(5,))
# [1 9 3 5 6]

print(x + y)
# [ 4 12  9  9 13]

print(np.add(x,y))
# [ 4 12  9  9 13]

print(x - y)
# [ 2 -6  3 -1  1]

print(np.subtract(x,y))
# [ 2 -6  3 -1  1]

print(x * y)
# [ 3 27 18 20 42]

print(np.multiply(x,y))
# [ 3 27 18 20 42]

print(x / y)
# [3.         0.33333333 2.         0.8        1.16666667]

print(np.divide(x,y))
# [3.         0.33333333 2.         0.8        1.16666667]

print(x + 3)
# [ 6  6  9  7 10]

t = np.array([1, 2, 3])
z = np.array([1, 2, 3])

print(np.array_equal(x,y))
# False

print(np.array_equal(t,z))
# True

print(np.sqrt(x))
# [1.73205081 1.73205081 2.44948974 2.         2.64575131]

print(np.power(x, 3))
# [ 27  27 216  64 343]

print(np.exp(x))
# [  20.08553692   20.08553692  403.42879349   54.59815003 1096.63315843]

print(np.sum(x))
# 23

