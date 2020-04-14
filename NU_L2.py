# урок 3, задания 2-3

# cats = {
#     "myCat":
#         {"name": "Kashtan",
#          "nose": "wet",
#          "tail": "fluffy",
#          "mustache": "long",
#          "tum": "soft",
#          "body parts":
#              {"legs": 4,
#               "ears": 2,
#               "tail": 1}
#          },
#     "anotherCat":
#         {"name": "Murzik",
#          "nose": "dry",
#          "tail": "fluffy",
#          "mustache": "short",
#          "tum": "soft",
#          "body parts":
#              {"legs": 4,
#               "ears": 2,
#               "tail": 1}
#          }
# }
# flag = True
# inputOption = input("Введите искомый параметр: ")
# inputValue = input("Введите значение искомого параметра: ")
#
# for i in cats:
#     if cats.get(i).get(inputOption) == inputValue:
#         print("Под эти параметры подходит котик по имени", cats.get(i).get("name"))
#         flag = False
# if flag:
#     print("Проверьте вводимые данные ИЛИ искомого котика нет")

# урок 3, задание 1
#
# cats = [
#     ["Kashtan", "wet nose", "fluffy tail", "long mustache", "soft tum"],
#     ["Murzik", "dry nose", "fluffy tail", "short mustache", "soft tum"]
# ]
#
# inputOption = input("Введите искомый параметр: ")
# for cat in cats:
#     if inputOption in cat:
#         print("Под искомые параметры подходит котик по имени", cat[0])

# # урок 4, задание 1
#
# import numpy
#
# print("Сумма ряда от 0 до 100 =", numpy.sum(numpy.array(range(100))))
#
# # # урок 4, задание 2
#
# a = int(input("Введите конечный элемент ряда: "))
# print("Сумма ряда от 0 до", a, "=", numpy.sum(numpy.array(range(a))))
#
# # урок 4, задание 3
#
# print("Среднее значение 100 случайных чисел = %f" % numpy.mean(numpy.random.randn(100)) )

# урок 5, задание 2
#
# test = {
#     "name": "Kashtan",
#     "nose": "wet",
#     "tail": "fluffy",
#     "mustache": "long",
#     "tum": "soft",
# }
# inputOption = input("Введите искомый параметр: ")
# inputValue = input("Введите значение искомого параметра: ")
#
# def searchInArray(inputOption, inputValue, array):
#     for i in array:
#         if array.get(inputOption) == inputValue:
#             return True
#
# if searchInArray(inputOption, inputValue, test):
#     print("Искомое значение параметра", inputOption, ":",inputValue, "есть в тестовом массиве", test)

# урок 5, задание 1

# test = ["Kashtan", "wet nose", "fluffy tail", "long mustache", "soft tum"]
# inputOption = input("Введите искомый параметр: ")
#
# def searchInArray(inputOption, string):
#     for i in string:
#         if inputOption in i:
#             return True
#
# if searchInArray(inputOption, test):
#     print("Искомое значение параметра", inputOption, "есть в тестовом массиве", test)

# урок 5, задание 3

inputString1 = "компьютер"
inputString2 = "компьютеризация"

def compare(S1, S2):
    ngrams = [
        S1[i:i+3] for i in range(len(S1))
    ]
    print(S1)
    count = 0
    for ngram in ngrams:
        count += S2.count(ngram)
    # return count/max(len(S1), len(S2))

# print(compare(inputString1, inputString2))