import requests

# print(requests.get('http://127.0.0.1:8000/items/rfwsdee').json())
# print(requests.get('http://127.0.0.1:8000/items?count=20').json())


print('Adding an item:')
print(
    requests.post(
        url='http://127.0.0.1:8000/',
        json={'name': 'Screwdriver',
              'price': 3.99,
              'count': 10,
              'id': 4,
              'category': 'tools'}
    ).json()
)
print(requests.get('http://127.0.0.1:8000/').json())
print('*' * 100)

print('Updating an item:')
print(requests.put('http://127.0.0.1:8000/update/0?count=9001').json())
print(requests.get('http://127.0.0.1:8000/').json())
print('*' * 100)

print('Deleting an item:')
print(requests.delete('http://127.0.0.1:8000/delete/0').json())
print(requests.get('http://127.0.0.1:8000/').json())
print('*' * 100)

print('Put errors')
print(requests.put('http://127.0.0.1:8000/update/0?count=-1').json())
print('*' * 100)
print(requests.put('http://127.0.0.1:8000/update/0?price=-2.1').json())
print('*' * 100)
print(requests.put('http://127.0.0.1:8000/update/-1').json())
print('*' * 100)
print(requests.put('http://127.0.0.1:8000/update/0?name=SuperUltraMegaHammer').json())
