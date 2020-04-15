# урок 6, задание 3

# множество объектов с параметрами завернуто в класс,
# реализован поиск значения в словаре из объектов через нечеткое сравнение строк

from pprint import pprint


def compare(S1, S2):
    ngrams = [
        S1[i:i + 3] for i in range(len(S1))
    ]

    count = 0
    for ngram in ngrams:
        count += S2.count(ngram)
    return count / max(len(S1), len(S2))


class Cat:
    def __init__(self, name, breed, nose, tail, mustache, tum):
        self.name, self.breed, self.nose, self.tail, self.mustache, self.tum = name, breed, nose, tail, mustache, tum
        self.key = (name, breed)

    def __repr__(self):
        return "Cat('%s','%s','%s','%s','%s','%s')" % (
            self.name, self.breed, self.nose, self.tail, self.mustache, self.tum)

    def __eq__(self, obj):
        if type(obj) == str:
            count = 0
            for x in [self.name, self.breed, self.nose, self.tail, self.mustache, self.tum]:
                if compare(obj, x) >= 0.5:
                    count += 1
            if count > 0:
                return True
            else:
                return False


Kashtan = Cat("Kashtan", "abyssinian", "wet", "fluffy", "long", "soft")
Murzik = Cat("Murzik", "bengal", "dry", "fluffy", "short", "soft")
Cats = {
    Kashtan.key: Kashtan,
    Murzik.key: Murzik,
}

inputValue = "sry"

for cat in Cats.values():
    if cat == inputValue:
        print("Нашелся котейка %s" % cat)
