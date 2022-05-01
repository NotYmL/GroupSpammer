import time, requests #imports

try:
    tokens=[]                           #make a list
    f = open('tokens.txt', 'r')         #load tokens.txt as read
    for token in f.read().split('\n'):  #for token in tokens.txt
        tokens.append(token)            #add token to list tokens
except Exception as err:                #If error print and exit
    print('==============\nError while loading tokens from tokens.txt\n==============\nError:\n', err)
    input()
    exit()

recipients=[]       #make a list

def Group_Make_request(token, recipients):      #define a function
    res=requests.post("https://canary.discord.com/api/v9/users/@me/channels", headers={         #make a group dm create request
        "authorization": str(token),
        "content-type": "application/json",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-context-properties": "eyJsb2NhdGlvbiI6Ik5ldyBHcm91cCBETSJ9",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "en-GB",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC40NiIsIm9zX3ZlcnNpb24iOiIxMC4wLjE5MDQzIiwib3NfYXJjaCI6Ing2NCIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImNsaWVudF9idWlsZF9udW1iZXIiOjEyNjMxMiwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
    },
    json={
        "recipients": recipients
    })

    return res  #return response

if(input('1. Load group recipients from file\n2. Input group recipients\n[1-2]: ')=='1'):   #input for recipients
    try:
        f = open(input('File name: '), 'r')     #get recipients from a file (max 9 !DO NOT PUT ID OF THE BOT!)
        for id in f.read().split('\n'):
            recipients.append(id)
    except Exception as err:
        print('==============\nError while loading recipients from file (Try with .txt)\n==============\nError:\n', err)
        input()
        exit()
else:
    print('Enter 0 when done')      #Input ids
    loop=True
    while(loop):
        id=input('User ID: ')
        if(id=='0'):
            loop=False
        else:
            recipients.append(id)
    
sleeptime=int(input('Sleep [s]: '))     #make a var for sleep time
print('Press CTRL+C to stop!')

try:
    while(True):
        for token in tokens:
            res=Group_Make_request(token, recipients)       #call request func
            print(res)                                      #print request response
            time.sleep(sleeptime)                           #sleep
        time.sleep(sleeptime)                               #sleep in while loop
except KeyboardInterrupt:                                   #stop on CTRL+C
    print('==============\nStoped\n==============')