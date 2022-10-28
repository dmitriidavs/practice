class ThreadData:
    __shared_attrs = {
        'name': 'thread_1',
        'data': {},
        'id': 1
    }

    def __init__(self):
        # в каждом экземпляре по default-у будут одни и те же свойства
        self.__dict__ = self.__shared_attrs


th1 = ThreadData()
th2 = ThreadData()

# при переопределении свойств или создании новых, для любого экземпляра
# класса пространство аттрибутов будет общим, определяющееся словарем
th2.id = 3
th1.attr_new = 'new_attr'

print(th1.__dict__)
print(th2.__dict__)
