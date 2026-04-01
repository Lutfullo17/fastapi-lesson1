from fastapi import FastAPI
from users.urls import router as router_users
from products.urls import router as router_products
# from admin.urls import router as router_admin

app = FastAPI()

app.include_router(router=router_users)
app.include_router(router=router_products)
# app.include_router(router=router_products)
