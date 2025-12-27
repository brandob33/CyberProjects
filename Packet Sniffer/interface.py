from scapy.all import *

for line in get_if_list():
    print(f'ID: {line} , IP: {get_if_addr(line)}')
