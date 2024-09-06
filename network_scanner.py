# #!/usr/bin/python
# import scapy.all as scapy
# import argparse
#
#
# # Function to parse command-line arguments
# def get_arguments():
#     parser = argparse.ArgumentParser(description="Network Scanner")
#     parser.add_argument("-t", "--target", dest="target", help="Target IP range (e.g., 192.168.0.1/24)")
#     options = parser.parse_args()
#
#     # If no target is provided, prompt the user
#     if not options.target:
#         parser.error("[-] Please specify a target IP range, use --help for more info.")
#     return options
#
#
# # Function to perform the network scan
# def scan(ip):
#     # Create an ARP request directed at the IP range
#     arp_request = scapy.ARP(pdst=ip)
#
#     # Create an Ethernet frame to broadcast the ARP request to all devices on the network
#     broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
#
#     # Combine the ARP request and Ethernet frame
#     arp_request_broadcast = broadcast / arp_request
#
#     # Send the packet and receive the response, setting timeout to 1 second
#     answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
#
#     # Create an empty list to hold the results
#     clients_list = []
#
#     # Process each response
#     for element in answered_list:
#         client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
#         clients_list.append(client_dict)
#
#     return clients_list
#
#
# # Function to display the scan results
# def print_result(results_list):
#     print("IP\t\t\tMAC Address\n-----------------------------------------")
#     for client in results_list:
#         print(client["ip"] + "\t\t" + client["mac"])
#
#
# # Main function
# options = get_arguments()
# scan_result = scan(options.target)
# print_result(scan_result)


import scapy.all as scapy
import argparse

from httpx import options


def get_arguments():
    parser = argparse.ArgumentParser(description='Scan the network')
    parser.add_argument("-t", "--target", dest="target")
    options = parser.parse_args()
    return options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    # return answered_list


    print("IP\t\t\tMAC Address\n-----------------------------------------")
    clients_list = []
    for element in answered_list:
        clients_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(clients_dict)
    return clients_list


def print_result(clients_list):
    for client in clients_list:
        print(client["ip"] + "\t\t" + client["mac"])

options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)