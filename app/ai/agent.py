from langgraph.graph import StateGraph
from utils.state import OrderAgentState
import utils.nodes as nodes

graph = StateGraph(OrderAgentState)

graph.add_node("receive", nodes.receive_input)
graph.add_node("ocr", nodes.ocr_node)
graph.add_node("parse", nodes.parse_node)


graph.set_entry_point("receive")

graph.add_conditional_edges(
    "receive",
    lambda state: nodes.receive_input(state),
    {
        "ocr": "ocr",
        "parse": "parse"
    }
)