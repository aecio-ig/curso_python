import os
from dotenv import load_dotenv
load_dotenv()

## remetente e destinatario
remetente = os.getenv('EMAIL','')
destinatario = remetente

#Configs
smpt_server = 'smtp.google.com'
smpt_port = 587
smpt