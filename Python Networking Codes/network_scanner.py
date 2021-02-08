import scapy.all as scapy

def scan(ip):
    arp_req = scapy.ARP(pdst = ip)
    #print arp_req.show()
    arp_broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    #print arp_broadcast.show()
    arp_req_broad = arp_broadcast/arp_req
    #print arp_req_broad.show()
    answered, unanswered = scapy.srp(arp_req_broad, timeout = 1, verbose = False) #srp is for send receive packet and the packet that is to be sent is arp_req_broad, timeout is the time for which it waits for the dest response in seconds and verbose=False is used to not print the additional details

    details_list = []
    # print "--------------------------------------------------------------------------"
    # print "IP Address\t\t\t\tMAC Address"
    # print "--------------------------------------------------------------------------"

    for element in answered:
        #print element          #Print both the sent and recived data
        #print element[1]       #Print the raw packet that is unreadable
        #print element[1].show()  #Print the packets in readable format
        #print element[1].psrc   #print the IP address of the client
        #print element[1].hwsrc   #Print the MAC address of the client
        details_dict = {"IP": element[1].psrc, "MAC": element[1].hwsrc}
        details_list.append(details_dict)
        #print element[1].psrc + "\t\t\t\t" + element[1].hwsrc

    return details_list

def print_list(details):

    print "--------------------------------------------------------------------------"
    print "IP Address\t\t\t\tMAC Address"
    print "--------------------------------------------------------------------------"

    for client in details:
        print client["IP"] + "\t\t\t\t" + client["MAC"]


details = scan("192.168.0.0/24")
print_list(details)





#element[1] contains the received packets whereas element[0] contains the sent packets
#.show and .summary provide details about the packet
#.ARP is used to create an IP based broadcast packet and .Ether is used to create a MAC based broadcast packet
#.srp is for Send Receive Packet
#print elemet would print both the sent and received packet
# scapy.ls(function) can be used to see what options does that fuction provide eg. scapy.ls(ARP()) or scapy.ls(Ether())
