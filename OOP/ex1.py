class Point:
    """
        Класс для представления координат точек на плоскости
    """
    def __new__(cls, *args, **kwargs):
        print(f'Вызов __new__ для {str(cls)}')
        return super().__new__(cls)

    def __init__(self, a, b):
        print(f'Вызов __init__ для {str(self)}')
        self.x = a
        self.y = b

    def set_coords(self, x, y):
        self.x = x
        self.y = y


class Database:
    """
        Реализация класса Database по паттерну Singleton
    """

    # ссылка на экземпляр класса
    __instance = None

    # этот метод нужен, чтобы в __init__ нельзя было переопределить локальные аттрибуты при повторном создании объекта
    # def __call__(self, *args, **kwargs):

    def __new__(cls, *args, **kwargs):
        # если None, то создаем новый экземпляр класса
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        # если уже существует, то просто возвращается адрес уже созданного объекта
        return cls.__instance

    def __del__(self):
        # в финализаторе ссылка на объект обнуляется
        Database.__instance = None

    def __init__(self, user, password, port):
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        print(f'Connection with DB: {self.user}, {self.password}, {self.port}')


class Vector:
    MIN_COORD = 0
    MAX_COORD = 100

    @classmethod    # работает только с аттрибутами класса, но не с аттрибутами экземпляра класса
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        # если координаты проходят проверку, то мы их меняем
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

        print(f'Квадрат нормы self: {self.norm2(self.x, self.y)}')

    # для обращения к аттрибутам экземпляра
    def get_coord(self):
        return self.x, self.y

    @staticmethod   # независимая сервисная функция, не имеющая доступа к cls или self
    def norm2(x, y):
        return x*x + y*y


if __name__ == '__main__':
    v = Vector(1, 10)
    print(Vector.validate(5))
    print(v.get_coord())
    print(f'Квадрат нормы: {v.norm2(2, 5)}')
