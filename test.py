from datetime import datetime
import requests
import json
print("#####################################################")
print("#               REQUEST AUTOMATER                   #")
print("#####################################################")
def start():
    return datetime.now()
def post(urls):
    requested=start()
    file1 = open('data.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        passing_data=json.loads(line.strip())
        print('[+]Requesting Data ['+str(passing_data)+']')
        r = requests.post(url = urls, data = passing_data)
        pastebin_url = r.text
        print('[+] RESULT')
        print(json.dumps(pastebin_url))
        responded=start()
        print('\nRequested on ['+str(requested)+']\n')
        print('\nResponded on ['+str(responded)+']\n')
def get(urls):
    requested=start()
    file1 = open('data.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        passing_data=json.loads(line.strip())
        print('[+]Requesting Data ['+str(passing_data)+']')
        r = requests.get(url = urls, data = passing_data)
        pastebin_url = r.text
        print('[+] RESULT')
        print(json.dumps(pastebin_url))
        responded=start()
        print('\nRequested on ['+str(requested)+']\n')
        print('\nResponded on ['+str(responded)+']\n')
def request_flood(url,type,round):
    if type=='1':
        print("---Get request---")
        for x in range(int(round)):
            get(url)

    if type=='2':
        print("---POST Request---")
        for x in range(int(round)):
            post(url)

url=input("Enter the api base url:")
print('Select request type\n1,GET\n2,POST')
type=input('Select Request type:')
round=input("Enter the count to load")

request_flood(url,type,round)
