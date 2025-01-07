start a virtaul using python
```
create a .env file with 
```
BOT_TOKEN=your-token-here
TESTING_GUILD_ID=1326191744022482954
```
install the requirements.txt
```py
pip install -r requirements.txt
```
then pull the default model
```
ollama pull orca-mini:3b
```
after pulling the default model run the bot by running 
```
run.py
```
To change the model open chat.py and change 
``` 
 for part in chat('orca-mini:3b', messages=messages, stream=True):
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