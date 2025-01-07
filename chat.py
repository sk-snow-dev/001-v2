from ollama import chat

def chatbot(user_input):
    """
    Chat with the Ollama chatbot.
    """
    messages = [{'role': 'user', 'content': user_input}]
    response = ""
    for part in chat('orca-mini:3b', messages=messages, stream=True):
        response += part['message']['content']
    return response
