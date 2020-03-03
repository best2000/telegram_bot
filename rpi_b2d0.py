import requests, re
from datetime import datetime



class telegram_bot:
    def __init__(self, token):
        self.token = token

    #All types used in the Bot API responses are represented as JSON-objects.

    def getUpdates(self, parameter):
        url = 'https://api.telegram.org/'+self.token+'/getUpdates'+parameter
        res = requests.request("GET", url)
        resdic = res.json() #convert json respond to python dict
        return resdic     

    def sendMessage(self, parameter):
        url = 'https://api.telegram.org/'+self.token+'/sendMessage'+parameter
        res = requests.request("GET", url)
        resdic = res.json() 
        return resdic  

    def sendPhoto(self, parameter):
        url = 'https://api.telegram.org/'+self.token+'/sendMessage'+parameter
        res = requests.request("GET", url)
        resdic = res.json() 
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
admin_id = 1012049725

#get lastest update_id
resdic = bot.getUpdates("")
while not resdic['result']:
    print("Stand By.", end='\r')
    resdic = bot.getUpdates("")
up_id = resdic['result'][-1]['update_id']+1

while True:
    resdic = bot.getUpdates("?offset="+str(up_id)+"&allowed_updates=[“message”]")
    if resdic['result']:
        try:
            if resdic['result'][0]['message']['entities'][0]['type'] == 'bot_command' and resdic['result'][0]['message']['from']['id'] == admin_id:
                def_msg = resdic['result'][0]['message']['text']
                msg = re.split(" ", def_msg)
                dt = datetime.utcfromtimestamp(int(resdic['result'][0]['message']['date'])).strftime('%Y-%m-%d %H:%M:%S')
                print(dt, ":", def_msg)
                
                if msg[0] == '/kill':
                    bot.sendMessage("?chat_id="+str(admin_id)+"&text=I'm dead.")
                    break
                elif msg[0] == '/cmd':
                    import subprocess
                    bot.sendMessage("?chat_id="+str(admin_id)+"&text=Plz wait.")
                    bot.sendMessage("?chat_id="+str(admin_id)+"&text=Don't interrupt me.")
                    subprocess.call([msg[i+1] for i in range(len(msg)-1)], shell=True)
                    bot.sendMessage("?chat_id="+str(admin_id)+"&text=Finished.")
        except:
            pass
        up_id = up_id+1
    else:
        print("Stand By.", end='\r')