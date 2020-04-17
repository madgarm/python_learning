from pprint import pprint
from utils import compare, int_val
from itertools import product

ADDRESS_WORDS = {'улица', 'живет', 'адрес'}
HOUSE_WORDS = {'дом', 'здание'}
ROOM_WORDS = {'квартира', 'кв', 'помещение'}
NAME_WORDS = {'имя', 'зовут'}
LASTNAME_WORDS = {'фамилия'}
AGE_WORDS = {'возраст', 'старше', 'младше', 'лет'}


class Person:
    def __init__(self, name, lastname, age, address, house, room):
        self.name, self.lastName, self.age, self.address, self.house, self.room = name, lastname, age, address, house, room
        self.key = (name, lastname, age)

    def __repr__(self):
        return "Person('%s','%s',%s,'%s',%s,%s)" % (self.name, self.lastName, self.age, self.address, self.house, self.room)

    def __eq__(self, obj):
        if type(obj) == Person:
            return (self.name, self.lastName, self.age, self.address, self.house, self.room) == (obj.name, obj.lastname, obj.age, obj.address, obj.house, obj.room)
        elif type(obj) == str:
            return self.__fuzzy_compare(obj)
        else:
            return self.__repr__() == obj.__repr__()

    def __fuzzy_compare(self, query):
        def by_address(Q):
            Q = Q - ADDRESS_WORDS
            W = set(self.address.replace(',', '').split())
            rez = []
            for a, b in product(Q, W):
                rez += [(compare(a, b), a, b)]
            return max(rez)[0]

        def by_house(Q):
            query_house = max([int_val(q) for q in Q])
            return query_house + 2 >= self.house >= query_house - 2

        def by_room(Q):
            query_room = max([int_val(q) for q in Q])
            return query_room + 3 >= self.room >= query_room - 3

        def by_name(Q):
            Q = Q - NAME_WORDS
            W = set(self.name.split())
            rez = []
            for a, b in product(Q, W):
                rez += [(compare(a, b), a, b)]

            return max(rez)[0]

        def by_lastName(Q):
            Q = Q - LASTNAME_WORDS
            W = set(self.lastName.split())
            rez = []
            for a, b in product(Q, W):
                rez += [(compare(a, b), a, b)]

            return max(rez)[0]

        def by_age(Q):
            query_age = max([int_val(q) for q in Q])
            if 'старше' in Q:
                return query_age < self.age
            if 'младше' in Q:
                return query_age > self.age
            return query_age + 5 >= self.age >= query_age - 5

        q_words = set(query.split())
        score = 0
        for m_words, method in zip([ADDRESS_WORDS, HOUSE_WORDS, ROOM_WORDS, NAME_WORDS, LASTNAME_WORDS, AGE_WORDS],
                                   [by_address, by_house, by_room, by_name, by_lastName, by_age]):
            if m_words & q_words:
                score += method(q_words)

        if score > 0.49:
            return True
        else:
            return False


lena = Person("Лена", "Петрова", 19, "Пушкина",  14, 115)
oleg = Person("Олег", "Иванов", 34, "Ленскoго", 10, 11)
olga = Person("Ольга", "Иванова", 28, "Онегина", 11, 12)
nata = Person("Наташа", "Сидорова", 17, "Ростова", 16, 15)

queries = [
    'имя Ольга',
    'фамилия Иванова',
    'возраст 30',
    'старше 20',
    'младше 20',
    'живет на Пушкина',
    'дом 10',
    'здание 13',
    'квартира 113',
    'кв 15',
    'фамилия ростова',
    'зовут нташа',
]

people = {
    lena.key: lena,
    oleg.key: oleg,
    olga.key: olga,
    nata.key: nata,
}

for query, person in product(queries, people.values()):
    if person == query:
        pprint((query, person))
    else:
        print("Не найдено: ", end="")
        pprint((query, person))
