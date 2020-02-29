import requests
from datetime import datetime



class telegram_bot:
    def __init__(self, token):
        self.token = token

    #All types used in the Bot API responses are represented as JSON-objects.

    def getUpdates(self, parameter):
        url = 'https://api.telegram.org/'+self.token+'/getUpdates'+parameter
        res = requests.get(url)
        resdic = res.json() #convert json respond to python dict
        return resdic     

    #WEBHOOK
    def setWebhook(self, parameter):
        url = 'https://api.telegram.org/'+self.token+'/setWebhook'+parameter
        res = requests.post(url)
        resdic = res.json() 
        print(resdic)

    def getWebhookInfo(self):
        url = 'https://api.telegram.org/'+self.token+'/getWebhookInfo'
        res = requests.get(url)
        resdic = res.json() 
        print(resdic)

    def deleteWebhook(self):
        url = 'https://api.telegram.org/'+self.token+'/deleteWebhook'
        res = requests.get(url)
        resdic = res.json() 
        print(resdic)


bot = telegram_bot('bot'+'1096258874:AAHtnfJpdm2_FPCHLChYHaEnZutzRsX7usU')

with open('up_id.txt', 'r') as f:
    up_id = int(f.readline()) 

while True:
    resdic = bot.getUpdates("?offset="+str(up_id)+",allowed_updates=[“message”]")
    if resdic['result'] != []:
        unixts = int(resdic['result'][0]['message']['date'])
        dt = datetime.utcfromtimestamp(unixts).strftime('%Y-%m-%d %H:%M:%S')
        text = resdic['result'][0]['message']['text']
        print(dt, ":", text)
        
        up_id += 1
        with open('up_id.txt', 'w') as f:
            f.write(str(up_id))

