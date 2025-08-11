from pydantic import BaseModel, ConfigDict, EmailStr  # Agregar ConfigDict
from datetime import datetime
from decimal import Decimal
from typing import List, Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal
    image_url: Optional[str] = None

class Product(ProductBase):
    id: int
    status: str
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

