#!/usr/bin/env python
import scapy.all as scapy
import optparse
import argparse


def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcat = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcat/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]
    client_list = []
    for element in answered_list:
        client_dic= {"IP": element[1].psrc, "MAC": element[1].hwsrc}
        client_list.append(client_dic)
    return client_list


def print_result(result_list):
    print("IP\t\t\tMAC Address\n ---------------------")
    for client in result_list:
        print(client["IP"] + "\t\t" + client["MAC"])


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="IP to Target")
    options, arguments = parser.parse_args()
    return options


options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)