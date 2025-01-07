import requests # type: ignore
import json

def chatbot(user_input):
    """
    Chat with the Ollama API.
    """
    # Define the API URL and model name
    url = "http://192.168.12.220:11434/api/chat"  # Ensure the correct endpoint is used
    model = "orca-mini:3b"  # Specify the model to use

    # Prepare the payload
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }

    try:
        # Send the POST request to the API
        response = requests.post(url, json=payload, stream=True)

        # Check if the request was successful
        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code} - {response.text}")

        # Accumulate the streamed response
        chat_response = ""
        for line in response.iter_lines(decode_unicode=True):
            if line.strip():
                # Decode the line to a string if it's in bytes
                decoded_line = line.decode('utf-8') if isinstance(line, bytes) else line
                # Parse the JSON response
                json_response = json.loads(decoded_line)
                # Append the content to the chat response
                chat_response += json_response["message"]["content"]

        return chat_response

    except requests.RequestException as e:
        return f"Error communicating with Ollama API: {str(e)}"
    except Exception as e:
        return str(e)