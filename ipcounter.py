#!/usr/bin/python
# coding=utf-8
# Author github.com/Eltotiz

import os
from colorama import Fore, init, Style
import fade
from shodan import Shodan
import json
import requests
import time

banner = """	    ________     ______                  __           
	   /  _/ __ \   / ____/___  __  ______  / /____  _____
	   / // /_/ /  / /   / __ \/ / / / __ \/ __/ _ \/ ___/
	 _/ // ____/  / /___/ /_/ / /_/ / / / / /_/  __/ /    
	/___/_/       \____/\____/\__,_/_/ /_/\__/\___/_/     
"""

# PLACE YOUR SHODAN KEY
# PLACE YOUR SHODAN KEY
# PLACE YOUR SHODAN KEY
# PLACE YOUR SHODAN KEY

api = Shodan('PLACE YOUR SHODAN KEY')

os.system("clear")

print("")

faded_text = fade.purplepink(banner)
print(faded_text)

print(Fore.GREEN + " 	    	   Created by github/eltotiz")
print("")

IP = input(" Insert the IP > ")
print("")
print(" [+] Connecting to the API ...")

api2 = f"""http://ip-api.com/json/{IP}"""
shodanIP = api.host(IP)



data = requests.get(api2).json()

os.system("clear")

print("")


faded_text = fade.purplepink(banner)
print(faded_text)


domain = format(shodanIP.get('hostnames'))
chars = ['[', ']', "'"]
res = domain.translate(str.maketrans('', '', ''.join(chars)))

ports = format(shodanIP.get('ports'))
chars = ['[', ']', "'"]
portstext = ports.translate(str.maketrans('', '', ''.join(chars)))

print(Fore.GREEN + " 	    	   Created by github/eltotiz")
print("")
print("")
print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ IP INFORMATION ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ")
print("")
print(' [!] IP Address: ', data['query'])
print(' [!] Status: ', data['status'])
print(' [!] Country: ', data['country'])
print(' [!] Country Code: ', data['countryCode'])
print(' [!] Region: ', data['region'])
print(' [!] Region Name: ', data['regionName'])
print(' [!] City: {}'. format(shodanIP.get('city')))
print(' [!] Zip: ', data['zip'])
print(' [!] Latitude: ', data['lat'])
print(' [!] Loginth', data['lon'])
print(' [!] Time zone: ', data['timezone'])
print(' [!] IPS: ', data['isp'])
print(f" [!] Domains: {res}")
print(' [!] Organization: ', data['org'])
print(' [!] AS: ', data['as'])
print(f' [!] Ports: {portstext}')
print("")
print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
print("")
print("")
print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ POSSIBLE EXPLOITS ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")
print("")
vulns = format(shodanIP.get('vulns', '                      N/A'))
chars = ['[', ']', "'"]
vulnstext = vulns.translate(str.maketrans('', '', ''.join(chars)))
print(f' {vulnstext}')
print("")
print(" ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄")


# Hello! :)