import requests
from typing import Annotated
from langchain.chat_models import AzureChatOpenAI
from langchain.agents import Tool
from langchain_core.messages import ToolMessage
from langchain.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict


# 1. Tool function: Get current weather for a city using OpenWeatherMap
def get_weather(city: str) -> str:
    api_key = "<YOUR_OPENWEATHERMAP_API_KEY>"  # <-- Replace with your key
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200 or "main" not in data:
            return f"Could not retrieve weather for '{city}'. Please check the city name."

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"The current weather in {city} is {desc} with a temperature of {temp}°C."

    except Exception as e:
        return f"Failed to get weather data: {str(e)}"


# 2. Tool definition
tools = [
    Tool.from_function(
        name="get_weather",
        func=get_weather,
        description="Get the current weather for a city. Input should be the city name.",
    )
]


# 3. Azure OpenAI model with tool binding
llm = AzureChatOpenAI(
    deployment_name="gpt-mini",     # Replace with your deployment name
    model="gpt-35-turbo",           # Should support tool calling
    api_version="2023-07-01-preview",
    temperature=0,
).bind_tools(tools)


# 4. LangGraph state
class State(TypedDict):
    messages: Annotated[list, add_messages]


# 5. Chatbot node with tool execution
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

        # Continue the conversation with tool results
        response = llm.invoke(messages + new_messages)
        new_messages.append(response)

    return {"messages": new_messages}


# 6. LangGraph builder
graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile()


# 7. Run
if __name__ == "__main__":
    state = {
        "messages": [
            {"role": "user", "content": "What's the weather like in Paris?"}
        ]
    }

    final_state = graph.invoke(state)
    for msg in final_state["messages"]:
        print(f"{msg.type.upper()}: {msg.content}")
