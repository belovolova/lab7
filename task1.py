import numpy as np
from random import randint
import time

time_start = time.perf_counter()  # замеряем время выполнения
# создаем два массива в 1 миллион элементов, заполненных случайными значениями чисел
m1 = []
m2 = []
for i in range(10000):
    m1 = np.append(m1, randint(1, 10 ** 10))
    m2 = np.append(m2, randint(1, 10 ** 10))

m_result = np.multiply(m1, m2)
print(m_result)
print(time.perf_counter() - time_start)  # поэлементно перемножаем массивы

# поэлементное перемножение двух массивов без использования библиотеки NumPy
# time_start = time.perf_counter()
# m1 = []
# m2 = []
# for i in range(1000000):
#     m1.append(randint(1, 10 ** 10))
#     m2.append(randint(1, 10 ** 10))
# i = 0
# m_result = []
# while i < len(m1):
#     c.append(m1[i] * m2[i])
#     i += 1
# print(m_result)
# print(time.perf_counter() - time_start)

# сравнив время выполнения операции поэлементного перемножения двух массивов с использованием библиотеки NumPy и без использования NumPy,
# можно сделать вывод о том, что с использованием библиотеки NumPy программа работает быстрее.
