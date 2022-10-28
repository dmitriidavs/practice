class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_coord(self, x, y):
        if self.MIN_COORD <= x <= self.MAX_COORD:
            self.x = x
            self.y = y

    # # def set_bound(self, left):
    # #     # создает новый локальный аттрибут - НЕ ПРАВИЛЬНО
    # #     self.MIN_COORD = left
    #
    # # ПРАВИЛЬНО
    # @classmethod
    # def set_bound(cls, left):
    #     cls.MIN_COORD = left

    def __getattribute__(self, item):
        # # вызывается, когда идет обращение к аттрибуту через экземпляр класса
        # # возвращает значение соответствующего аттрибута
        # print('__getattribute__')
        # # через стандартный объект Python
        # return object.__getattribute__(self, item)

        # если бы хотели запретить доступ к какому-либо аттрибуту
        if item == 'x':
            raise ValueError('Access denied')
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        # # вызывается, когда идет присвоение аттрибуту какого-либо значения
        # print('__setattr__')
        # object.__setattr__(self, key, value)
        # если бы хотели запретить создавать аттрибут с определенным именем
        if key == 'z':
            raise AttributeError('Invalid attribute name')
        else:
            object.__setattr__(self, key, value)
            # # # присвоение будет выполняться по рекурсии - НЕ ПРАВИЛЬНО
            # # self.x = value
            # # ПРАВИЛЬНО
            # self.__dict__[key] = value

    def __getattr__(self, item):
        # # вызывается, когда идет обращение к несуществующему аттрибуту экземпляра класса
        # print('__getattr__: ' + item)

        # чтобы убрать ошибку обращения к несуществующему аттрибуту
        return False

    def __delattr__(self, item):
        print('__delattr__: ' + item)
        # без вызова функции стандартного класса удаления не произойдет
        object.__delattr__(self, item)


pt1 = Point(1, 2)
pt2 = Point(10, 20)

del pt1.x
print(pt1.__dict__)
