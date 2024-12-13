from scapy.all import *
import random

spoof_ip = "192.168.113.115"

targets = ["192.168.113.1","192.168.113.2","192.168.113.3","192.168.113.4","192.168.113.5","192.168.113.6","192.168.113.7","192.168.113.8","192.168.113.9","192.168.113.10"]


for ip in targets:
	for x in range(1, 11):
		packet = IP(src=spoof_ip, dst=ip)/TCP(sport=random.randint(4000,5000), flags="S")
		send(packet)
		
