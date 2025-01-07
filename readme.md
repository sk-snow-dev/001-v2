start a virtaul env using 
```
source venv/bin/activate
python
```
create a .env file with 
```
BOT_TOKEN=your-token-here
TESTING_GUILD_ID=1326191744022482954
```
run 
```py
pip install -r requirements.txt
```
then run
```
ollama pull orca-mini:3b
```
To change the mode
```py open chat.py and change 
 for part in chat('orca-mini:3b', messages=messages, stream=True):
```
To
```py
for part in chat('your-modelname', messages=messages, stream=True):
```
