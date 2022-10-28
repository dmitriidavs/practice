# class Geom(object):   # эквивалентно
class Geom:
    pass


class Line(Geom):
    pass


g = Geom()
l = Line()
print(l.__class__)
# проверка принадлежности класса другому классу
print(issubclass(Line, Geom))
print(issubclass(Geom, Line))
# проверка принадлежности экземпляра классу
print(isinstance(l, Geom))
print(isinstance(l, object))
print(isinstance(Geom, object))
# стандартные типы данных тоже классы и наследуются от стандартного object
print(isinstance(int, object))


# расширение типа данных с помощью переопредеоения пользовательского вывода
class Vector(list):
    # pass
    def __str__(self):
        # к каждому объекту списка применяем функцию str и полученные строки записываем через пробел
        return ' '.join(map(str, self))


v = Vector([1, 2, 3])
print(v)
print(type(v))
