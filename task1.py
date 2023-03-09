import numpy as np
from random import randint
import time
######################
time_start = time.perf_counter()
m1 = []
m2 = []
for i in range(10000):
    m1 = np.append(m1, randint(1, 10 ** 10))
    m2 = np.append(m2, randint(1, 10 ** 10))

m_result = np.multiply(m1, m2)
print(m_result)
print(time.perf_counter()-time_start)
