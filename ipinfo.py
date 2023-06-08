import requests
import json

ip_address = ''
def infoip(ip_address):
	response = requests.get('http://ip-api.com/json/' + ip_address)
	data = json.loads(response.text)
	print("IP Address:  ", data['query'])
	print("ISP:         ", data['isp'])
	print("City:        ", data['city'])
	print("Country:     ", data['country'])
	print("Region:      ", data['regionName'])
	print("Timezone:    ", data['timezone'])
	print("Postal Code: ", data['zip'])
	print("ASN:         ", data['as'])
	print("Location:    ", data['lat'],data['lon'])

def checkip(ip_address):
	ip_address = input("Enter Your IP: ")
	if ip_address == '127.0.0.1':
		print("Err.. IP Address Is not valid !!")
		return checkip(ip_address)
	else :
		print(infoip(ip_address))

print(' ___ ____    ___        __')
print('|_ _|  _ \  |_ _|_ __  / _| ___')
print(' | || |_) |  | ||  _ \| |_ / _ \ ')
print(' | ||  __/   | || | | |  _| (_) |')
print('|___|_|     |___|_| |_|_|  \___/')
print()
print('Craeted By NOMO TEAM')
print()
print('Telegram Channel: https://AnonymousHackersNM.t.me')
print('YouTube Channel: https://youtube.com/@NOMOHACK')
print()
print()
print(checkip(ip_address))
#Created By NOMO TEAM
#Channel Telegram: https://AnonymousHackersNM.t.me
#Channel YouTube: https://youtube.com/@NOMOHACK
