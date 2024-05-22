"""
    Product Schema
"""
from typing import Optional
from decimal import Decimal
from pydantic import BaseModel


class ProductSchema(BaseModel):
    """
        Class ProductSchema
    """
    id: Optional[int] = None
    name: str
    description: str
    price: Decimal
