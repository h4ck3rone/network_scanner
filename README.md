Network Scanner
Overview
This Python-based Network Scanner is a simple tool for discovering devices on a local network. It sends ARP requests to a specified IP range and retrieves the IP and MAC addresses of devices that respond. Built using the powerful Scapy library, this tool is perfect for network administrators, cybersecurity enthusiasts, or anyone looking to map out devices on their local network.

Features
Scans a specified IP range using ARP (Address Resolution Protocol).
Displays IP and MAC addresses of responsive devices.
Easy-to-use command-line interface.
Lightweight and fast network scanning.
Built with Python and Scapy for high flexibility and customizability.

How it Works
Sends ARP requests to all IP addresses within a specified range.
Broadcasts the requests to the local network to identify devices.
Collects responses containing the IP and MAC addresses of devices that reply.

Requirements
Python 3.x
Scapy library

Install Scapy using pip:
pip install scapy

Usage
Run the network scanner with the following command:

sudo python3 network_scanner.py --target <IP Range>

Example:
sudo python3 network_scanner.py --target 192.168.1.1/24
Example Output
less
IP                  MAC Address
-----------------------------------------
192.168.1.1         aa:bb:cc:dd:ee:ff
192.168.1.2         ff:ee:dd:cc:bb:aa
Customization
You can customize the tool for more advanced tasks like:

Scanning specific ports.
Adding support for more protocols (e.g., ICMP, TCP).
Logging the results to a file for analysis.
License
This project is licensed under the MIT License - see the LICENSE file for details.

