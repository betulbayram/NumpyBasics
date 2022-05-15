import numpy as np
# import time

# start_time = time.time()
# A = np.arange(1000000)
# A ** 2

# time_1 = time.time()-start_time

# start_time2 = time.time()
# L = range(1000000)
# [i ** 2 for i in L]

# time_2 = time.time()-start_time2

# print(time_2/time_1)


x = np.array([4,5,6,7])#elemanlar aynı data tipine sahip

print(type(x))  #classını verir  o: <class 'numpy.ndarray'>
print(x.shape)  #her boyut için eleman sayısı tuple olarak doner o: (4,)
print(x.size)   #oluşturduğu toplam eleman sayısı o: 4
print(x.ndim)   #boyutunu verir o: 1
print(x.nbytes) #depolama için kullanılan byte miktari o: 16
print(x.dtype)  #elemanların veri tipini belirtir o: int32

y = np.array([[3,5,6,7], [3,5,8,9]])
print(type(y))
print(y.shape)
print(y.size)
print(y.ndim)
print(y.nbytes)
print(y.dtype)
