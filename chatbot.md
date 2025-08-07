If your LLM (e.g., Azure OpenAI deployment) does not support function/tool calling, here are your main options:

Option: Manual Tool Triggering (Function Detection via Prompt Parsing)
Instead of relying on the LLM to automatically call tools, you can manually inspect its output, detect if a tool is needed (based on intent or keywords), and call the function yourself.

🔧 Implementation Outline

def chatbot(state: State):
    messages = state["messages"]
    response = llm.invoke(messages)

    new_messages = [response]

    # Detect tool call manually
    content = response.content.lower()
    if "weather" in content:
        # crude keyword-based detection
        city = extract_city(content)  # <-- you can improve this with regex or LLM extraction
        result = get_weather(city)
        new_messages.append({"role": "tool", "content": result})

        # Re-ask LLM to summarize tool output
        response = llm.invoke(messages + new_messages)
        new_messages.append(response)

    return {"messages": new_messages}
