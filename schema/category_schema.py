"""
Category Schema
"""
from datetime import datetime

from pydantic import BaseModel, ConfigDict


#schema for returning a category
class CategorySchema(BaseModel):
    """
    Class Category Schema
    """
    id : str
    name : str
    description: str
    date_created : datetime

    model_config = ConfigDict(
        from_attributes= True
    )


#schema for creating a category
class CategoryCreateSchema(BaseModel):
    """
    Class Category Create Schema
    """
    name: str
    description: str

    model_config = ConfigDict(
        from_attributes= True,
        json_schema_extra={
            "example":{
                "name":"Sample name",
                "description" : "Sample description"
            }
        }
    )
