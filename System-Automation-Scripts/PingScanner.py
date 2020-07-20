#!/usr/bin/python3
# Automation with scapy
import sys
from scapy.all import *
ip = sys.argv[1]            # command line argument
icmp = IP(dst=ip)/ICMP()
#icmp = IP(dst=ip)/TCP()
#IP defines the protocol for IP addresses
#dst is the destination IP address
#TCP defines the protocol for the ports
resp = sr1(icmp,timeout=10)
if resp == None:
    print("This host is down")
else:
    print("This host is up")
        
