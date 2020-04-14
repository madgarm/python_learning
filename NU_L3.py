# урок 3, задание 1

# поиск в списке по значению от пользователя

# cats = [
#     ["Kashtan", "wet nose", "fluffy tail", "long mustache", "soft tum"],
#     ["Murzik", "dry nose", "fluffy tail", "short mustache", "soft tum"]
# ]
#
# inputOption = input("Введите искомый параметр: ")
# for cat in cats:
#     if inputOption in cat:
#         print("Под искомые параметры подходит котик по имени", cat[0])

# урок 3, задания 2-3

# поиск в словаре по параметру и значению от пользователя

cats = {
    "myCat":
        {"name": "Kashtan",
         "nose": "wet",
         "tail": "fluffy",
         "mustache": "long",
         "tum": "soft",
         "body parts":
             {"legs": 4,
              "ears": 2,
              "tail": 1}
         },
    "anotherCat":
        {"name": "Murzik",
         "nose": "dry",
         "tail": "fluffy",
         "mustache": "short",
         "tum": "soft",
         "body parts":
             {"legs": 4,
              "ears": 2,
              "tail": 1}
         }
}
flag = True
inputOption = input("Введите искомый параметр: ")
inputValue = input("Введите значение искомого параметра: ")

for i in cats:
    if cats.get(i).get(inputOption) == inputValue:
        print("Под эти параметры подходит котик по имени", cats.get(i).get("name"))
        flag = False
if flag:
    print("Проверьте вводимые данные ИЛИ искомого котика нет")
