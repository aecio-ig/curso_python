import keyboard
import pyautogui
from dotenv import load_dotenv
import os
import time
load_dotenv()


binds = [
    {'bind': 'ctrl+shift+1', 'env_pair': 'SENHA_IGERP'},
    {'bind': 'ctrl+shift+2', 'env_pair': 'SENHA_SERVIDO'},
]

# tratar binds
binds = [(bind['bind'], os.getenv(bind['env_pair'])) for bind in binds]

def add_bind(bind, text):
    def digita():
        time.sleep(1)
        pyautogui.write(text)
    
    keyboard.add_hotkey(bind , digita)

for bind, env_pair in binds:
    add_bind(bind, env_pair)



print("Iniciando digitador danadin!")
keyboard.wait()  
