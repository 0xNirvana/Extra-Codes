#!/usr/bin/env python

import subprocess #Used to perform terminal commands using python
import optparse #used to create option menu that is used in command line arguements
import re       #used for regular expressions in python

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface",
                      help="Enter the Interface name whose MAC is to be changed.")
    parser.add_option("-m", "--mac-address", dest="new_mac", help="Enter the new MAC Address.")
    (options, arguements) = parser.parse_args()  # Parses all the mentioned options
    if not options.interface:
        parser.error("[-] Please enter a value for the interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please enter a value for new MAC, use --help for more info")
    else:
        return options

def change_mac(interface, new_mac):
    print ("[+] Changing MAC for: " + interface + " to " + new_mac)

    # This prevents command injection
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


# interface = options.interface
# new_mac = options.new_mac
# Method to ask user to enter values using input function
# interface = input("Enter the interface: ")
# new_mac = input("Enter the New MAC: ")

# Not used in order to avoid command injection
# subprocess.call("ifconfig " + interface + " down", shell=True)
# subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
# subprocess.call("ifconfig " + interface + " up", shell=True)

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])

    string_from_regex = re.search(r"(([0-9a-fA-F]{2})[:]){5}[0-9a-zA-Z]{2}", ifconfig_result)

    if string_from_regex:
        return str(string_from_regex.group(0))
    else:
        print ("[-] Could not read MAC Address")


options= get_args()
current_mac = get_current_mac(options.interface)
print "Current MAC Address is: ", current_mac
change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
print "Current MAC Address is: ", current_mac

if options.new_mac == current_mac:
    print "[+] MAC Changed Successfully"
else:
    print "[-] MAC was not changed"
