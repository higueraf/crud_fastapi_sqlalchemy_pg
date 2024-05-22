"""
Main Store API
"""
import uuid
from typing import List

from fastapi import FastAPI, Response
from sqlalchemy.ext.asyncio import async_sessionmaker
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from db import engine
from model.category import Category
from schema.category_schema import CategoryCreateSchema, CategorySchema
from schema.product_schema import ProductSchema
from services.category_service import CategoryService
from services.product_service import ProductService

# Create instance FastAPI
app = FastAPI()
app.title = "Store API with FastAPI"
app.version = "0.1.1"
product_service = ProductService()

@app.get('/', tags=['Hello World'])
def hello_world():
    """
    Main Endpoint
    """
    return {"message": "Hello World!"}

@app.get('/hello-friends', tags=['Hello Friends'])
def hello_friends():
    """
    Main Endpoint
    """
    return {"message": "Hello Friends!"}

# CRUD Product with Psycopg
@app.get('/api/product', tags=['Product with Psycopg'], status_code=HTTP_200_OK)
def read_all():
    """
    Read All Products
    """
    items = []
    for data in product_service.read_all():
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["name"] = data[1]
        dictionary["description"] = data[2]
        dictionary["price"] = data[3]
        items.append(dictionary)
    return items

@app.get('/api/product/{id}', tags=['Product with Psycopg'], status_code=HTTP_200_OK)
def read_one(product_id: str):
    """
    Read One Product
    """
    data = product_service.read_one(product_id)
    dictionary = {}
    dictionary["id"] = data[0]
    dictionary["name"] = data[1]
    dictionary["description"] = data[2]
    dictionary["price"] = data[3]
    return dictionary


@app.post('/api/product', tags=['Product with Psycopg'], status_code=HTTP_201_CREATED)
def create_product(product_data:ProductSchema):
    """
    Create Product
    """
    data = dict(product_data)
    data.pop("id")
    product_service.create(data)
    return Response(status_code=HTTP_201_CREATED)


@app.put('/api/product/{id}', tags=['Product with Psycopg'], status_code=HTTP_204_NO_CONTENT)
def update(product_data:ProductSchema, product_id: str):
    """
    Update Product
    """
    data = dict(product_data)
    data["id"] = product_id
    product_service.update(data)
    return Response(status_code=HTTP_204_NO_CONTENT)

@app.delete('/api/product/{product_id}', tags=['Product with Psycopg'], status_code=HTTP_204_NO_CONTENT)
def delete(product_id: str):
    """
    Delete Product
    """
    product_service.delete(product_id)
    return Response(status_code=HTTP_204_NO_CONTENT)



#create an async session object for Category CRUD
session = async_sessionmaker(bind=engine, expire_on_commit=False)

db = CategoryService()


@app.get("/categories", tags=['Categories with Sqlalchemy'],
         response_model=List[CategorySchema], status_code=HTTP_200_OK)
async def get_all_categories():
    """API endpoint for listing all category resources
    """
    categories = await db.get_all(session)

    return categories


@app.post("/categories", tags=['Categories with Sqlalchemy'], status_code=HTTP_201_CREATED)
async def create_category(category_data: CategoryCreateSchema) -> dict:
    """API endpoint for creating a category resource
    Args:
        category_data (CategoryCreateScheme): 
        data for creating a category using the category schema
    Returns:
        dict: category that has been created
    """
    new_category = Category(
        id=str(uuid.uuid4()), name=category_data.name, description=category_data.description
    )
    category = await db.create(session, new_category)
    return category


@app.get("/category/{category_id}", tags=['Categories with Sqlalchemy'], status_code=HTTP_200_OK)
async def get_category_by_id(category_id) -> dict:
    """API endpoint for retrieving a category by its ID

    Args:
        category_id (str): the ID of the category to retrieve

    Returns:
        dict: The retrieved category
    """
    category = await db.get_by_id(session, category_id)
    print(category)
    return category


@app.patch("/category/{category_id}", tags=['Categories with Sqlalchemy'], status_code=HTTP_204_NO_CONTENT)
async def update_category(category_id: str, data: CategoryCreateSchema):
    """Update by ID

    Args:
        category_id (str): ID of category to update
        data (CategoryCreateScheme): data to update category

    Returns:
        dict: the updated category
    """
    category = await db.update(
        session, category_id, data={"name": data.name, "description": data.description}
    )

    return category


@app.delete("/category/{category_id}", tags=['Categories with Sqlalchemy'], status_code=HTTP_204_NO_CONTENT)
async def delete_category(category_id) -> None:
    """Delete category by id

    Args:
        category_id (str): ID of category to delete

    """

    await db.delete(session, category_id)
