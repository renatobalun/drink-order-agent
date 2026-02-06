from pydantic import BaseModel

class OrderItemClass(BaseModel):
    item_id: int
    name: str
    unit: str
    packaging: str
    quantity: int