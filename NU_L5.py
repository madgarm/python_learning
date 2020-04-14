# урок 5, задание 1

# поиск в списке по значению от пользователя (как функция)

# test = ["Kashtan", "wet nose", "fluffy tail", "long mustache", "soft tum"]
# inputOption = input("Введите искомый параметр: ")

# def searchInArray(inputOption, string):
#     for i in string:
#         if inputOption in i:
#             return True

# if searchInArray(inputOption, test):
#     print("Искомое значение параметра", inputOption, "есть в тестовом массиве", test)

# урок 5, задание 2

# поиск в словаре по параметру и значению от пользователя (как функция)

# test = {
#     "name": "Kashtan",
#     "nose": "wet",
#     "tail": "fluffy",
#     "mustache": "long",
#     "tum": "soft",
# }
# inputOption = input("Введите искомый параметр: ")
# inputValue = input("Введите значение искомого параметра: ")

# def searchInArray(inputOption, inputValue, array):
#     for i in array:
#         if array.get(inputOption) == inputValue:
#             return True

# if searchInArray(inputOption, inputValue, test):
#     print("Искомое значение параметра", inputOption, ":",inputValue, "есть в тестовом массиве", test)

# урок 5, задание 3

cats = {
    "myCat":
        {"name": "Kashtan",
         "nose": "wet",
         "tail": "fluffy",
         "mustache": "long",
         "tum": "soft"
         },
    "anotherCat":
        {"name": "Murzik",
         "nose": "dry",
         "tail": "fluffy",
         "mustache": "short",
         "tum": "soft"
         }
}


def compare(S1, S2):
    ngrams = [
        S1[i:i + 3] for i in range(len(S1))
    ]

    count = 0
    for ngram in ngrams:
        count += S2.count(ngram)
    return count / max(len(S1), len(S2))


# сюда вводим искомое значение, например set
inputValue = "set"


def searchInArray(input, array):
    for i in array:
        for j in array.get(i):
            if compare(array.get(i).get(j), input) >= 0.50:
                print("Найдено с коэффициентом похожести %f" % compare(array.get(i).get(j), input), "для котика",
                      array.get(i))


searchInArray(inputValue, cats)
