import os
import sys

#getting saved profiles
saved_profiles = os.popen('netsh wlan show profiles').read()

#getting availabale profiles
available_profiles = os.popen("netsh wlan show networks").read()
print(available_profiles)

#Asking user to choose the prefered network
preferred_ssid=input('Enter the preferred wifi for your connection:')


#if prefered network is not in saved profiles we will exit
#else we will disconnect the present connected network
if preferred_ssid not in saved_profiles:
    print("profile for"+preferred_ssid+" is not saved in profiles")
    print("sorry but can't establish the connection")
    sys.exit()
else:

    print("profile for"+preferred_ssid+" is  saved in profiles")
    response=os.popen("netsh wlan disconnect").read()
    print(response)
#while going through all the available networks we will find prefered network

while True:
	avail = os.popen('netsh wlan show networks').read()
	if preferred_ssid in avail:
		print("found")
		break

print("....Connecting...")

#Lastly connecting to prefered network

resp = os.popen('netsh wlan connect name=' + '"' + preferred_ssid + '"').read()
print(resp)
