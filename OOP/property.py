# class Person:
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         self.__age = age
#
#     age = property(get_age, set_age)


class Person:
    """
    О том, как работать с приватными закрытыми локальными аттрибутами
    Обращение / Переобозначение / Удаление
    """

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age


p = Person('Серега', 20)
# p.__dict__['old'] = 'old in object p'
# property имеет наибольший приоритет
p.age = 23
del p.age
p.age = 5
print(p.__dict__)
print(p.__doc__)
