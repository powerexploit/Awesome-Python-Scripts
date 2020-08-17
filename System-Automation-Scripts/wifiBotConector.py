import os
import sys

saved_profiles = os.popen('netsh wlan show profiles').read()
#print(saved_profiles)

available_profiles = os.popen("netsh wlan show networks").read()
print(available_profiles)

preferred_ssid=input('Enter the preferred wifi for your connection:')



if preferred_ssid not in saved_profiles:
    print("profile for"+preferred_ssid+" is not saved in profiles")
    print("sorry but can't establish the connection")
    sys.exit()
else:
	
    print("profile for"+preferred_ssid+" is  saved in profiles")
    response=os.popen("netsh wlan disconnect").read()
    print(response)


while True:
	avail = os.popen('netsh wlan show networks').read()
	if preferred_ssid in avail:
		print("found")
		break

print("....Connecting...")

resp = os.popen('netsh wlan connect name=' + '"' + preferred_ssid + '"').read()
print(resp)