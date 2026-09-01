from fastapi import FastAPI,Response;
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class product(BaseModel):
    id : Optional[int] = None
    name: str
    price: int
    description: str

products = []
id = 0

@app.post("/product")
def create_product(product: product,response: Response):
    global id
    try:
        id += 1
        product.id = id
        products.append(product)
        response.status_code = 201
        return {"isSuccess": True, "message": "Product created successfully"}
    except Exception as e:
        response.status_code = 500
        return {"message": "error creating the product","isSuccess": False}


        

@app.get("/products/{id}")
def get_product(id: int, response: Response):
    for product in products:
        if product.id == id:
            response.status_code = 200
            return {
                "isSuccess": True,
                "data": product
            }

    response.status_code = 404
    return {
        "isSuccess": False,
        "message": "Product not found"
    }


@app.put("/products/{id}")
def update_product(id: int, product: product, response: Response):
    for i in range(len(products)):
        if products[i].id == id:
            product.id = id
            products[i] = product
            response.status_code = 200
            return {"isSuccess": True,"message": "Product updated successfully","data": product}

    response.status_code = 404
    return {"isSuccess": False,"message": "Product not found"}


@app.delete("/products/{id}")
def delete_product(id: int, response: Response):
    for i in range(len(products)):
        if products[i].id == id:
            products.pop(i)
            response.status_code = 200
            return {"isSuccess": True,"message": "Product deleted successfully"}

    response.status_code = 404
    return {"isSuccess": False,"message": "Product not found"}