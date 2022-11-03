from pydantic import (
    BaseModel,
    ValidationError,
    Field,
    validator,
    root_validator
)


# class Tag(BaseModel):
#     id: int
#     tag: str
#
#
# # модель данных - описание структуры данных
# class City(BaseModel):
#     city_id: int
#     name: str
#     tags: list[Tag]
#
#
# input_json = """
# {
#     "city_id": "777",
#     "name": "Moscow",
#     "tags": [
#     {
#         "id": 1, "tag": "capital"
#     }, {
#         "id": 2, "tag": "big city"
#     }
#     ]
# }
# """
#
# try:
#     city = City.parse_raw(input_json)
# except ValidationError as e:
#     print("Exception:", e.json())
# else:
#     tag = city.tags[1]
#     print(tag.json())


class City(BaseModel):
    city_id: int
    # camelCase -> snake_case
    name: str = Field(alias='cityFullName')

    @root_validator
    def should_have_selected_field(cls, values):
        print('values', values)
        return values

    @validator('name')
    def name_should_be_spb(cls, v: str) -> str:
        if 'spb' not in v.lower():
            raise ValueError('Only SPb allowed!')
        return v


# class UserWithoutPassword(BaseModel):
#     name: str
#     email: str
#
#
# class User(UserWithoutPassword):
#     password: str


input_json = """
{
    "city_id": "132",
    "cityFullName": "Spb"
}
"""

try:
    city = City.parse_raw(input_json)
except ValidationError as e:
    print("Exception:", e.json())
else:
    print(city.json())
    # output as original
    print(city.json(by_alias=True))
    # exclude fields (e.g. exclude password hash)
    print(city.json(by_alias=True,
                    exclude={"city_id"}))
