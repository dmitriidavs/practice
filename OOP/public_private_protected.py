# from accessify import private, protected - здесь private сильнее, чем __method,
# т.к. после этого декоратора обратиться к методу с помощью pt._Point__method нельзя


class Point:

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y

    # приватный метод (cls - ссылка на класс Point)
    # @private
    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    # setter
    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Coordinates should be in (int, float)')

    # getter
    def get_coord(self):
        return self.__x, self.__y


pt = Point(1, 2)
pt.set_coord(10, 20)
