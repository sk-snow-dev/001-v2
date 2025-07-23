# Getting Started

1. Create a virtual environment using Python

2. Create a `.env` file with the following content:
    ```
    BOT_TOKEN=your-token-here
    TESTING_GUILD_ID=1326191744022482954
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Pull the default model:
    ```bash
    ollama pull orca-mini:3b
    ```

5. Start the bot:
    ```bash
    python run.py
    ```

## Changing the Model

To use a different model, modify `chat.py` and update the following line:
```python
 model = "orca-mini:3b"    
```
To
```
for part in chat('your-modelname', messages=messages, stream=True):
```
To also change the ollama requst url change 
```
url = "http://192.168.12.220:11434/api/chat"
``` 
in chat.py to 
```
url = "http://you-chat-ip:your-chat-port/api/chat"
```