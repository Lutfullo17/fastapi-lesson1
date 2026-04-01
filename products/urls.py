from fastapi import APIRouter, Request

router = APIRouter(prefix='/product')

@router.get("/")
async def products_2():
    return {"olma, anor"}


@router.get("/app13")
async def products_25():
    return {"None"}

@router.post("/data")
async def yubotr(request: Request):
    data = await request.json()
    return {'name': data.get('name'), 'age': data.get('age')}


from pydantic import BaseModel
class Product(BaseModel):
    title: str
    price: int
@router.post("/product")
async def yuborish(product:Product):
    return {"Title": product.name, "price": product.age}
