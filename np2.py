import numpy as np

x = np.array([1, 2, 4.4, 7])
np.save("dosya_1", x)

y = np.load("dosya_1.npy")