# урок 4, задание 1

# с numpy подсчет суммы рядо от 0 до 100

# import numpy
# print("Сумма ряда от 0 до 100 =", numpy.sum(numpy.array(range(100))))

# урок 4, задание 2

# с numpy подсчет суммы рядо от 0 до введенного пользователем числа

# a = int(input("Введите конечный элемент ряда: "))
# print("Сумма ряда от 0 до", a, "=", numpy.sum(numpy.array(range(a))))

# урок 4, задание 3

# с numpy подсчет среднего значения 100 случайных чисел

import numpy
print("Среднее значение 100 случайных чисел = %f" % numpy.mean(numpy.random.randn(100)) )