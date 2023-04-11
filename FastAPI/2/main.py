from enum import Enum
from typing import Optional

from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel

app = FastAPI()


class Category(Enum):
    TOOLS = 'tools'
    CONSUMABLES = 'consumables'


class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    category: Category


items = {
    0: Item(name='Hammer', price=9.99, count=20, id=0, category=Category.TOOLS),
    1: Item(name='Pliers', price=5.99, count=20, id=1, category=Category.TOOLS),
    2: Item(name='Nails', price=1.99, count=100, id=2, category=Category.CONSUMABLES),
}


@app.get('/')   # GET root URL
def index() -> dict[str, dict[int, Item]]:
    return {'items': items}


@app.get('/items/{item_id}')   # GET item by id
def query_item_by_id(item_id: int) -> Item:
    if item_id not in items:
        raise HTTPException(
            status_code=404, detail=f'Item with {item_id=} doesn\'t exist.'
        )
    return items[item_id]


@app.get('/items/')
def query_item_by_params(name: Optional[str] = None,
                         price: Optional[float] = None,
                         count: Optional[int] = None,
                         category: Optional[Category] = None) -> dict:

    def check_item(item: Item) -> bool:
        return all(
            (
                name is None or item.name == name,
                price is None or item.price == price,
                count is None or item.count == count,
                category is None or item.category == category,
            )
        )

    selection = [item for item in items.values() if check_item(item)]
    print(selection)

    return {
        'query': {'name': name, 'price': price, 'count': count, 'category': category},
        'selection': selection
    }


@app.post('/')
def add_item(item: Item) -> dict[str, Item]:

    if item.id in items:
        HTTPException(
            status_code=400, detail=f'Item with {item.id=} already exists.'
        )

    items[item.id] = item
    return {'added': item}


@app.put(
    '/update/{item_id}',
    responses={
        404: {'description': 'Item not found'},
        400: {'description': 'No args specified'},
    },
)
def update(item_id: int = Path(ge=0),   # item_id >= 0
           name: Optional[str] = Query(default=None, min_length=1, max_length=8),   # 1 <= len(name) <= 8
           price: Optional[float] = Query(default=None, gt=0.0),    # price > 0.0
           count: Optional[int] = Query(default=None, ge=0)) -> dict[str, Item]:

    if item_id not in items:
        HTTPException(
            status_code=400, detail=f'Item with {item_id=} does not exist.'
        )
    if all(info is None for info in (name, price, count)):
        raise HTTPException(
            status_code=400, detail='No parameters provided for update.'
        )

    item = items[item_id]
    if name is not None:
        item.name = name
    if price is not None:
        item.price = price
    if count is not None:
        item.count = count

    return {'updated': item}


@app.delete('/delete/{item_id}')
def delete_item(item_id: int) -> dict[str, Item]:

    if item_id not in items:
        raise HTTPException(
            status_code=400, detail=f'Item with {item_id=} does not exist.'
        )

    item = items.pop(item_id)

    return {'deleted': item}
