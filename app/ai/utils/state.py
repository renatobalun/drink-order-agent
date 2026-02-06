from typing import List, Literal
from typing_extensions import TypedDict
from app.classes.order_item import OrderItemClass

class OrderAgentState(TypedDict):
    raw_input: str
    ocr_text: str
    source_type: Literal["TEXT", "IMAGE"]
    parsed_lines: List[str]
    items_proposed: List[str]
    items_resolved: List[OrderItemClass]
    description: List[str]
    payment_method: str
    user_command: str
    confirmed: bool
    