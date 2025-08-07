"""
export OPENAI_API_TYPE=azure
export OPENAI_API_BASE=https://<your-resource-name>.openai.azure.com/
export OPENAI_API_KEY=<your-azure-key>
export OPENAI_API_VERSION=2023-07-01-preview
"""

from typing import Annotated
from langchain.chat_models import AzureChatOpenAI
from langchain.agents import Tool
from langchain_core.messages import ToolMessage
from langchain.tools.render import format_tool_to_openai_function
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

# 1. Tool function: convert km to miles
def convert_km_to_miles(km: float) -> str:
    miles = km * 0.621371
    return f"{km} kilometers is equal to {miles:.2f} miles."


# 2. Wrap tool for LangChain
tools = [
    Tool.from_function(
        name="convert_km_to_miles",
        func=convert_km_to_miles,
        description="Convert kilometers to miles. Takes a float as input.",
    )
]

# 3. Azure OpenAI model with function calling enabled
llm = AzureChatOpenAI(
    deployment_name="gpt-mini",  # Your Azure deployment name
    model="gpt-35-turbo",        # Azure model family
    api_version="2023-07-01-preview",
    temperature=0,
).bind_tools(tools)


# 4. LangGraph state
class State(TypedDict):
    messages: Annotated[list, add_messages]


# 5. LangGraph chatbot node with tool calling
def chatbot(state: State):
    messages = state["messages"]
    response = llm.invoke(messages)

    new_messages = [response]

    if response.tool_calls:
        for tool_call in response.tool_calls:
            tool = next((t for t in tools if t.name == tool_call["name"]), None)
            if tool:
                result = tool.invoke(tool_call["args"])
                new_messages.append(ToolMessage(content=result, tool_call_id=tool_call["id"]))

        # Reinvoke LLM with tool results
        response = llm.invoke(messages + new_messages)
        new_messages.append(response)

    return {"messages": new_messages}


# 6. LangGraph definition
graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile()

# 7. Run
if __name__ == "__main__":
    state = {
        "messages": [
            {"role": "user", "content": "How many miles is 15 kilometers?"}
        ]
    }
    final_state = graph.invoke(state)
    for msg in final_state["messages"]:
        print(f"{msg.type.upper()}: {msg.content}")
