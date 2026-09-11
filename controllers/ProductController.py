from fastapi import FastAPI, Response
from ProductModel import Product
import productcontroller


app = FastAPI()





@app.post("/product")
def create_product(product: Product, response: Response):

    try:

        product = productcontroller.create_product(product)

        response.status_code = 201

        return {
            "isSuccess": True,
            "message": "Product created successfully",
            "data": product
        }

    except Exception:

        response.status_code = 500

        return {
            "isSuccess": False,
            "message": "Error creating the product"
        }


@app.get("/products/{id}")
def get_product(id: int, response: Response):

    product = productcontroller.get_product(id)

    if product:

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
def update_product(id: int, product: Product, response: Response):

    updated_product = productcontroller.update_product(id, product)

    if updated_product:

        response.status_code = 200

        return {
            "isSuccess": True,
            "message": "Product updated successfully",
            "data": updated_product
        }

    response.status_code = 404

    return {
        "isSuccess": False,
        "message": "Product not found"
    }


@app.delete("/products/{id}")
def delete_product(id: int, response: Response):

    deleted_product = productcontroller.delete_product(id)

    if deleted_product:

        response.status_code = 200

        return {
            "isSuccess": True,
            "message": "Product deleted successfully"
        }

    response.status_code = 404

    return {
        "isSuccess": False,
        "message": "Product not found"
    }