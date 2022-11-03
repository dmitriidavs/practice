# from typing import List


# class ShoppingCart:
#
#     def __init__(self, max_size: int) -> None:
#         self.items: List[str] = []
#         self.max_size = max_size
#
#     def add(self, item: str):
#         if self.size() == self.max_size:
#             raise OverflowError('Cannot add more items')
#         self.items.append(item)
#
#     def size(self) -> int:
#         return len(self.items)
#
#     def get_items(self) -> List[str]:
#         return self.items
#
#     def get_total_price(self, map_object):
#         total_price = 0
#         for item in self.items:
#             # total_price += price_map[item]
#             total_price += map_object.get(item)
#
#         return total_price

# import random
# lst = []
# for _ in range(10):
#     lst.append(random.randint(-10,10))
#
# import re
# print(os.name)

import re
string = 'This is a simple test message for test'
found = re.findall(r'test', string)

print(found)
