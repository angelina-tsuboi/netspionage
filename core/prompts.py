from prompt_toolkit import prompt
from core.scanner import scanner_choice
from core.reconnaissance import recon_choice
from core.detection import detect_choice
from core.print_output import print_output, print_input
import configparser

config = configparser.ConfigParser()
config.read('configuration.ini')
interface = config.get('Settings', 'WiFiInterface')

def print_banner():
       return (r"""
                __             _
    ____  ___  / /__________  (_)___  ____  ____ _____ ____
   / __ \/ _ \/ __/ ___/ __ \/ / __ \/ __ \/ __ `/ __ `/ _ \
  / / / /  __/ /_(__  ) /_/ / / /_/ / / / / /_/ / /_/ /  __/
 /_/ /_/\___/\__/____/ .___/_/\____/_/ /_/\__,_/\__, /\___/
                    /_/                        /____/
""")

def print_details():
    return("""
 Created by Angelina Tsuboi [angelinatsuboi.net] V.0.0.1

 https://github.com/ANG13T/netspionage
 ----------------------------------------------------------------------------
       """)

def menu_display():
    return ("""
 ENTER 1 - 4 TO SELECT OPTIONS

 1.  SCANNING                   Scan for IPs, nearby APs, ports, hosts, and more

 2.  RECONNAISSANCE             Gather  information  about nearby MAC addresses

 3.  DETECTION                  Detect for ARP Spoofing and SYN Flood attacks

 4.  EXIT                       Exit from netspionage to your terminal
       """)

def prompt_display():
    print_output(print_banner())
    print_output(print_details())
    print_output(menu_display())
    while 1:
        user_input = print_input("\n netspionage >> ")
        if len(user_input)==0:
            print_output("\n")
            continue
        if user_input == "help" or user_input == "options" or user_input == "commands":
            print_output(menu_display())
            continue

        try:
            choice = int(user_input)
        except ValueError:
            print_output("\n Invalid Command! Type `help` to see all options")
            continue

        if choice == 1:
            while 1:
                print_output("\n 1. Network Scanner \n\n 2. WiFi Scanner \n\n 3. Port Scanner \n")
                resp = print_input(" SCAN INPUT >> ")
                target = ""
                if resp == "1" or resp == "3":
                    target = print_input(" NET IP ADDRESS (Eg: 192.168.1.1/24) >> ")
                break
            scanner_choice(resp, target, interface)
            continue

        if choice == 2:
            while 1:
                print_output("\n 1. Choose MAC Address \n\n 2. Input MAC Address\n")
                resp = print_input(" RECON INPUT >> ")
                target = ""
                if resp == "1":
                    target = print_input(" NET IP ADDRESS (Eg: 192.168.1.1/24) >> ")
                manual_input = ""
                if resp == "2":
                    manual_input = print_input(" MAC ADDRESS (Eg:08:00:69:02:01:FC) >> ")
                break
            recon_choice(resp, target, manual_input)
            continue

        if choice == 3:
            while 1:
                print_output("\n 1. ARP Spoof Attack \n\n 2. SYN Attack\n")
                resp = print_input(" DETECT INPUT >> ")
                target = print_input(" NET IP ADDRESS (Eg: 192.168.1.1/24) >> ")
                tcp = ""
                if resp == "2":
                    tcp = print_input(" TCP NUMBER (Eg: 80) >> ")
                break
            detect_choice(resp, target, tcp, interface)
            continue

        elif choice == 4:
            exit('\n Till next time!')

        else:
            pass

try:
    prompt_display()
except KeyboardInterrupt:
    quit('\n Till next time!')
