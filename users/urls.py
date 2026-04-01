from fastapi import APIRouter, Request

router =  APIRouter(prefix="/users")

@router.get('/')
async def users_list():
    return {'Laziz, Aziz'}

@router.get('/user1')
async def users_1():
    return {'Lutfullo Rizoyev'}



@router.post("/data")
async def yubotr(request: Request):
    data = await request.json()
    return {'title': data.get('title'), 'price': data.get('price')}


from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
@router.post("/data1")
async def yuborish(user:User):
    return {"name": user.name, "age": user.age}

