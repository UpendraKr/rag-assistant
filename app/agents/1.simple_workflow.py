from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class AgentState(TypedDict):
    question: str
    answer: str


def process_question(state: AgentState):
    question = state["question"]

    return {
        "answer": f"You asked: {question}"
    }

builder = StateGraph(AgentState)

# graoph node
builder.add_node(
    "process_question",
    process_question,
)

# Graph entry point.
builder.add_edge(
    START,
    "process_question",
)

# Graph exit point.
builder.add_edge(
    "process_question",
    END,
)

# Builds an executable graph.
graph = builder.compile()

# Executes the graph.
result = graph.invoke({
    "question": "What is FastAPI?",
    "answer": "",
})

print(result)