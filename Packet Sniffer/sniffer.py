from scapy.all import *
from dotenv import load_dotenv
import os

load_dotenv()

# Note npcap must be installed 
def handler(packet):
    if packet.haslayer(IP):
        print(packet.summary())

if __name__ == "__main__":
    ifacen = os.getenv('interface')
    sniff(iface=ifacen, prn=handler, count = 1)