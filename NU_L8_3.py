# урок 8, задание 3

# гадалка, запоминает ответы, пытается понять ввод

import random


def compare(S1, S2):
    ngrams = [
        S1[i:i + 3] for i in range(len(S1))
    ]

    count = 0
    for ngram in ngrams:
        count += S2.count(ngram)
    return count / max(len(S1), len(S2))


question = ""
questions = {}

while question != "Стоп":
    x = 0
    question = input("Задай свой вопрос: ")
    if question[-1] == "?" and question != "Стоп":
        if len(questions) == 0:
            a = random.randint(0, 1)
            print("Да") if a == 1 else print("Нет")
            questions[question] = a
        else:
            temp = questions.copy()
            for i in temp.keys():
                if compare(question, i) >= 0.5:
                    x += 1
            if x > 0:
                print("Ты уже спрашивал")
            else:
                a = random.randint(0, 1)
                print("Да") if a == 1 else print("Нет")
                questions[question] = a
    elif question == "Стоп":
        print(questions)
    else:
        print("Задай вопрос, я не понимаю")
