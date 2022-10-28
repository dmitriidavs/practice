class Goods:
    def __init__(self, name, weight, price):
        # инициализирует поиск init аттрибутов в MixinLog, т.к. MixinLog стоит позже по зависимостям
        super().__init__()
        print('Init Goods')
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f'{self.name}, {self.weight}, {self.price}')


# независимый класс, добавляющий функционал логирования товар с использованием их ID
class MixinLog:
    ID = 0

    def __init__(self):
        super().__init__()
        print('Init MixinLog')
        MixinLog.ID += 1
        self.id = MixinLog.ID

    def save_sell_log(self):
        print(f'{self.id}: товар продан в 00:00 часов')

    def print_info(self):
        print(f'print_info из класса MixinLog')


# class MixinLog2:
#     def __init__(self):
#         super().__init__()
#         print('Init MixinLog 2')


# сначала аттрибуты init будут искаться в Goods, потом в MixinLog
class NoteBook(Goods, MixinLog):
    # если нужно всегда вызывать метод именно из класса MixinLog
    def print_info(self):
        MixinLog.print_info(self)


n = NoteBook('Acer', 1.5, 30000)
n.print_info()
# n.save_sell_log()
# print(NoteBook.__mro__)
