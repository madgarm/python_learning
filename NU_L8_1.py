# урок 8, задание 1

# гадалка на минималках

import numpy

option = [0, 1]
a = numpy.random.choice(option)

question = input()

if question[-1] == "?":
    if a == 1:
        print("Да")
    else:
        print("Нет")
else:
    print("Задай вопрос, я не понимаю")
