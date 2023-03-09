import numpy as np
from time import perf_counter
from random import randint

start = perf_counter()  # определяем начальный момент времени

array_1 = np.random.randint(1, 1000000000, 1000001)  # создаем два массива произвольных целых чисел numpy
array_2 = np.random.randint(1, 1000000000, 1000001)
result_array = np.multiply(array_1, array_2)  # выполняем поэлементное перемножение элементов заданных массивов

# # поэлементное перемножение двух массивов без использования библиотеки NumPy
# array_1 = [randint(1, 1000000000) for i in range(1000001)]  # создаем два массива произвольных целых чисел
# array_2 = [randint(1, 1000000000) for i in range(1000001)]
# result_array = []  # результирующий массив
# length = len(array_1)  # записываем длину массивов в переменную
# for i in range(length):
#     result_array.append(array_1[i] * array_2[i])  # выполняем поэлементное перемножение элементов с записью в массив

print(perf_counter() - start)  # выводим время работы программы
