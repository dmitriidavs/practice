import requests

# print(requests.get('http://127.0.0.1:8000/items/rfwsdee').json())
print(requests.get('http://127.0.0.1:8000/items?count=20').json())
