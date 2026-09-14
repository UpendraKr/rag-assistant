import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.core.config import settings
from typing import TypedDict

from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from langgraph.prebuilt import ToolNode


# -------------------------
# State
# -------------------------

class AgentState(TypedDict):
    messages: list


# -------------------------
# Tool
# -------------------------

@tool
def calculator(expression: str) -> str:
    """Calculate a mathematical expression."""

    try:
        result = eval(
            expression,
            {"__builtins__": {}},
        )

        return str(result)

    except Exception:
        return "Unable to calculate expression."


# -------------------------
# LLM
# -------------------------

llm = ChatOpenAI(
    model=settings.LLM_MODEL,
    api_key=settings.OPENAI_API_KEY,
    temperature=0,
)

llm_with_tools = llm.bind_tools(
    [calculator]
)


# -------------------------
# LLM Node
# -------------------------

def call_llm(state: AgentState):

    response = llm_with_tools.invoke(
        state["messages"]
    )

    return {
        "messages": [response]
    }


# -------------------------
# Tool Node
# -------------------------

tools = [calculator]

tool_node = ToolNode(tools)


# -------------------------
# Router
# -------------------------

def should_continue(state: AgentState):

    last_message = state["messages"][-1]

    if getattr(last_message, "tool_calls", None):
        return "tools"

    return END


# -------------------------
# Graph
# -------------------------

builder = StateGraph(AgentState)

builder.add_node(
    "llm",
    call_llm,
)

builder.add_node(
    "tools",
    tool_node,
)

builder.add_edge(
    START,
    "llm",
)

builder.add_conditional_edges(
    "llm",
    should_continue,
)

builder.add_edge(
    "tools",
    "llm",
)

graph = builder.compile()


# -------------------------
# Run
# -------------------------

result = graph.invoke({
    "messages": [
        {
            "role": "user",
            "content": "What is 125 * 48?"
        }
    ]
})

print(
    result["messages"][-1].content
)