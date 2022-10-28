class Geom:
    name = 'Geom'

    def __init__(self, x1, y1, x2, y2):
        print(f'Инициализатор Geom для {self.__class__}')
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):

    # дочерний класс переопределяет базовый класс
    def draw(self):
        print('Рисование линии')


class Rect(Geom):
    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)    # делегирование, вызывая инициализатор базового класса
        print('Инициализатор Rect')
        self.fill = fill

    # дочерний класс переопределяет базовый класс
    def draw(self):
        print('Рисование прямоугольника')


l = Line(0, 0, 10, 20)
r = Rect(1, 2, 3, 4)
print(r.__dict__)
