from typing import TypedDict


class AgentState(TypedDict):
    question: str
    plan: list[str]
    results: list[str]
    answer: str


def planner_node(state: AgentState):

    question = state["question"]

    plan = []

    if "student" in question.lower() or "students" in question.lower():
        plan.append("Get student information using SQL")

    if "admission" in question.lower():
        plan.append("Search admission information using RAG")

    if not plan:
        plan.append("Answer the question directly")

    return {
        "plan": plan
    }


def executor_node(state: AgentState):

    plan = state["plan"]

    results = []

    for task in plan:

        if "SQL" in task:
            result = execute_readonly_sql(
                "SELECT COUNT(*) FROM students"
            )

            results.append(
                f"SQL Result: {result}"
            )

        elif "RAG" in task:
            result = search_knowledge(
                "admission process"
            )

            results.append(
                f"RAG Result: {result}"
            )

    return {
        "results": results
    }


from langchain_core.messages import HumanMessage


def synthesizer_node(state: AgentState):

    question = state["question"]
    results = state["results"]

    prompt = f"""
    Answer the user's question using the information below.

    Question:
    {question}

    Information:
    {results}

    Give a clear and concise answer.
    """

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    return {
        "answer": response.content
    }


# build graph
from langgraph.graph import StateGraph, START, END


builder = StateGraph(AgentState)

builder.add_node("planner", planner_node)
builder.add_node("executor", executor_node)
builder.add_node("synthesizer", synthesizer_node)

builder.add_edge(START, "planner")
builder.add_edge("planner", "executor")
builder.add_edge("executor", "synthesizer")
builder.add_edge("synthesizer", END)

graph = builder.compile()


result = graph.invoke({
    "question": "How many students are there and what is the admission process?",
    "plan": [],
    "results": [],
    "answer": ""
})

print(result["answer"])