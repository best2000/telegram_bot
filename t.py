import requests
from datetime import datetime



class telegram_bot:
    def __init__(self, token):
        self.token = token

    #All types used in the Bot API responses are represented as JSON-objects.

    def getUpdates(self):
        url = 'https://api.telegram.org/'+self.token+'/getUpdates'
        res = requests.get(url)
        resdic = res.json() #convert json respond to python dict
        print(resdic)
        #for i in resdic['result']:
            #print(datetime.utcfromtimestamp(i['message']['date']).strftime('%Y-%m-%d %H:%M:%S'), ":", i['message']['text'])

bot = telegram_bot('bot'+'1096258874:AAHtnfJpdm2_FPCHLChYHaEnZutzRsX7usU')
bot.Update()

#data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
#headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#r = requests.post(url, data=json.dumps(data), headers=headers)