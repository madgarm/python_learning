# урок 8, задание 2

# гадалка в цикле, запоминает связку вопрос-ответ
# проверяет вопросы на ранее задававшиеся

import random

question = ""
questions = {}

while question != "Стоп":
    question = input("Задай свой вопрос: ")
    if question[-1] == "?" and question != "Стоп":
        if question in questions.keys():
            print("Ты уже спрашивал")
        else:
            a = random.randint(0, 1)
            print("Да") if a == 1 else print("Нет")
            questions[question] = a
    else:
        print("Задай вопрос, я не понимаю")

print(questions)
