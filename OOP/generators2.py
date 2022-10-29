import csv
from typing import Generator


def gen_data(filename1: str) -> Generator:
    with open(filename1, 'r') as f:
        reader = csv.reader(f)
        yield next(reader)
        for row in reader:
            yield row


g = gen_data('data\\LTV.csv')
print('Column names:')
for col_name in next(g):
    print(f'| {col_name} |')
print('*'*150)
print(next(g))
print(next(g))
print(next(g))
