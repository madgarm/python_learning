# класс Cat включает объекты cat
# объектами, включенными в класс Cat, будут являться конкретные котики, наследующие от класса структуру параметров
# и методы работы с ними, но имеющие свои значения параметров, кроме тех, что назначены по умолчанию
# Cat - класс, поэтому называем существительным, с большой буквы
# названия объектов будут с маленькой буквы, типа murzik


class Cat:
    # стандартный метод, инициализация, здесь же задаем параметры
    def __init__(self):
        pass

    # стандартный метод, вовзращает формальное строковое представление
    def __repr__(self):
        pass

    # стандартный метод, метод сравнения с чем-либо
    def __eq__(self, **kwargs):
        pass

    # нестандартный метод, метод поиска по фразе
    # отглагольное название, т.к. метод, подразумевает действие
    def search(self, query):
        pass

    # нестандартный метод, гладим кота, он меняет значение одного из параметров (например)
    # отглагольное название, т.к. метод, подразумевает действие
    def stroke(self, obj):
        pass
