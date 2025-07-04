"""Use a dummy Graph for a dummy RAG application
1. Conditional edges
2. Looping logic
"""

import random
from pprint import pprint
from typing import TypedDict, Optional

from langgraph.graph import StateGraph, START, END


class AgentState(TypedDict):
    query: str
    meta_questions: Optional[list[str]] = []
    docs: Optional[list[str]] = []
    response: Optional[str] = None


def retriever(state: AgentState) -> AgentState:
    """Retrieve relevant documents from the vector database"""
    state["docs"] = [
        "Document1",
        "Document2",
        "Document3",
        "Document4",
        "Document5",
    ]
    return state


def llm(state: AgentState) -> AgentState:
    """Query the LLM and get the response"""
    state[
        "query"
    ] += f". These are the related documents to deduce the answer from {state['docs']} \n\n"
    state["response"] = "This is a dummy response by the dummy LLM trained by me 😊"
    return state


def meta_questions(state: AgentState) -> AgentState:
    state["meta_questions"] = [
        "How experienced is this person?",
        "Why does it look so good?",
        "Was he also learning LangGraph?",
    ]
    return state


def llm_as_judge(state: AgentState):
    return random.choice(["correct", "wrong"])


def main():
    graph = StateGraph(AgentState)

    # Nodes
    graph.add_node("retriever", retriever)
    graph.add_node("llm", llm)
    graph.add_node("questions", meta_questions)

    # Edges
    graph.add_edge(START, "retriever")
    graph.add_edge("retriever", "llm")
    graph.add_conditional_edges(
        source="llm",
        path=llm_as_judge,
        path_map={"correct": "questions", "wrong": "retriever"},
    )
    graph.add_edge("questions", END)

    app = graph.compile()
    pprint(
        app.invoke(
            input=AgentState(
                query="Who wrote this simple, good looking code",
            )
        )
    )


if __name__ == "__main__":
    main()
