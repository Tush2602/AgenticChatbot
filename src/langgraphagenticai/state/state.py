from typing_extensions import TypedDict
from typing import Annotated, List
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class State(TypedDict):
    """
    Represent the structure of the state used in graph.
    """
    messages: Annotated[List[BaseMessage], add_messages]
