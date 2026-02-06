from langchain_openai import ChatOpenAI
from app.core.config import OPENAI_API_KEY
from app.ai.utils.state import OrderAgentState

llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)

def receive_input(state: OrderAgentState):
    if state["source_type"] == "IMAGE":
        return "ocr"
    else:
        return "parse"
    
def ocr_node(state: OrderAgentState):
    #napravi ocr
    return

def parse_node(state: OrderAgentState):
    #parsiraj text
    return