#!/usr/local/bin/python3
# return local and public ip address

import socket
import requests

def get_local_IP():
    try:
        host_name = socket.gethostname()
        local_ip = socket.gethostbyname(host_name)
        print("Local IP: ", local_ip)
    except:
        print("Unable to get Local IP")


def get_public_IP():
    try:
        public_ip = requests.get('http://www.icanhazip.com').content.decode()
        print("Public IP: ", public_ip)
    except:
        print("Unable to get Public IP")


get_local_IP()
get_public_IP()
