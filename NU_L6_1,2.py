# урок 6, задание 1-2


from pprint import pprint


class Cat:
    def __init__(self, name, breed, nose, tail, mustache, tum):
        self.name, self.breed, self.nose, self.tail, self.mustache, self.tum = name, breed, nose, tail, mustache, tum
        self.key = (name, breed)

    def __repr__(self):
        return "Cat('%s','%s','%s','%s','%s','%s')" % (
            self.name, self.breed, self.nose, self.tail, self.mustache, self.tum)

    def __eq__(self, obj):
        if type(obj) == str:
            return obj in [self.name, self.breed, self.nose, self.tail, self.mustache, self.tum]


Kashtan = Cat("Kashtan", "abyssinian", "wet", "fluffy", "long", "soft")
Murzik = Cat("Murzik", "bengal", "dry", "fluffy", "short", "soft")
Cats = {
    Kashtan.key: Kashtan,
    Murzik.key: Murzik,
}

inputValue = "dry"

for cat in Cats.values():
    if cat == inputValue:
        print("Нашелся котейка %s" % cat)
