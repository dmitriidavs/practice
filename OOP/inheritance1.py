# родительский класс
class Geom:
    name = 'Geom'

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        print('Рисование геометрии')


# дочерний класс
class Line(Geom):
    name = 'Line'

    def draw(self):
        print('Рисование линии')


# дочерний класс
class Rect(Geom):
    pass
    # def draw(self):
    #     print('Рисование прямоугольника')


l = Line()
r = Rect()
l.set_coords(1, 1, 2, 2)
r.set_coords(1, 1, 2, 2)
# сначала аттрибут name ищется в дочернем классе, затем в родительском
print(l.name)
print(r.name)

l.draw()
r.draw()
