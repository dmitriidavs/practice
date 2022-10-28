class Geom:
    __name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f'Инициализатор Geom для {self.__class__}')
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._name = self.__name

    def _verify_coord(self, coord):
        return 0 <= coord < 100

    # def get_coords(self):
    #     return self.__x1, self.__y1


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill='red'):
        super().__init__(x1, y1, x2, y2)    # делегирование, вызывая инициализатор базового класса
        print('Инициализатор Rect')
        self._verify_coord(x1)
        self.__fill = fill

    # выдаст ошибку, т.к. не имеет доступа (если __att)
    def get_coords(self):
        return (self._x1, self._y1)


r = Rect(0, 0, 10, 20)
print(r.get_coords())
# приватные аттрибуты формируются по имени класса, в котором они прописаны
print(r._x1)
print(r.__dict__)
