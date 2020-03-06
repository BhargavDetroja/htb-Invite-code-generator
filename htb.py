#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import base64
import json
import os

os.system("clear")
CVIOLET = '\33[35m'
CBLINK    = '\33[5m'	
RED = '\033[1;31m'
BLUE = '\033[94m'
BOLD = '\033[1m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
WHITE = '\033[0m'



Title = CVIOLET \
    + """                                                                                                                                                                                                     
 
 _    _            _      _______ _            ____            
| |  | |          | |    |__   __| |          |  _ \           
| |__| | __ _  ___| | __    | |  | |__   ___  | |_) | _____  __
|  __  |/ _` |/ __| |/ /    | |  | '_ \ / _ \ |  _ < / _ \ \/ /
| |  | | (_| | (__|   <     | |  | | | |  __/ | |_) | (_) >  < 
|_|  |_|\__,_|\___|_|\_\    |_|  |_| |_|\___| |____/ \___/_/\_\


 _____            _ _                           _____          _        ______ _                _           
|_   _|          (_) |                         / ____|        | |      |  ____(_)              | |          
  | |  _ ____   ___| |_ __ _ ___  ___  _ __   | |     ___   __| | ___  | |__   _  ___ _ __   __| | ___ _ __ 
  | | | '_ \ \ / / | __/ _` / __|/ _ \| '_ \  | |    / _ \ / _` |/ _ \ |  __| | |/ _ \ '_ \ / _` |/ _ \ '__|
 _| |_| | | \ V /| | || (_| \__ \ (_) | | | | | |___| (_) | (_| |  __/ | |    | |  __/ | | | (_| |  __/ |   
|_____|_| |_|\_/ |_|\__\__,_|___/\___/|_| |_|  \_____\___/ \__,_|\___| |_|    |_|\___|_| |_|\__,_|\___|_| 
                                                               
                                                                          
\033[1;34m [*] www.hackthebox.eu Invite Code Generator [*]    
                                                                  
\033[1;34m Devloper:\033[32m Bhargav Detroja                                 
\033[1;34m It's For Lazy Hacker            
-----------------------------------------------------------------------------
""" \
    + WHITE

print Title

print "\033[1;31m [*] Start Hacking"

print "\033[1;31m [*] Hackthebox invite Code"

print "\033[0m [*] connect to server hackthebox.eu ..."

print "\033[0m [*] Collect Info to hackthebox.eu ..."

print "\033[33m [*] Decrept Invitason code"

print "\033[1;34m [*] Invite Code :\033[32m",base64.b64decode(requests.post("https://www.hackthebox.eu/api/invite/generate", json={"key": "value"}).json()["data"]["code"])
	
