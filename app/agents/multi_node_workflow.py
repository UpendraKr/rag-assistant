from typing import TypedDict
from langgraph.graph import StateGraph, START, END


class AgentState(TypedDict):
    question: str
    answer: str


def get_question(state: AgentState):
    return {
        "question": state["question"].strip()
    }

def generate_answer(state: AgentState):
    question = state["question"]

    return {
        "answer": f"You asked: {question}"
    }
    
builder = StateGraph(AgentState)

builder.add_node("get_question", get_question)
builder.add_node("generate_answer", generate_answer)

builder.add_edge(START, "get_question")
builder.add_edge("get_question", "generate_answer")
builder.add_edge("generate_answer", END)

graph = builder.compile()

# Executes the graph.
result = graph.invoke({
    "question": "What is FastAPI?",
    "answer": "",
})

print(result)