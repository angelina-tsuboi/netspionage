from scapy.all import Ether, ARP, srp, sniff, conf

def detect_choice(choice, target):
    if choice == '1':
        arp_detection()
        return()
    elif choice == '2':
        tcp_flood_detection(target)
        return()
    else:
        exit()

# Interface
iface="wlan0

def arp_detection():
    sniff(store=False, prn=process_arp, iface=iface)

def tcp_flood_detection(target):
    sniff(prn=flow_labels, store=0)

# Helper Functions

def get_mac(ip):
    p = Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip)
    result = srp(p, timeout=3, verbose=False)[0]
    return result[0][1].hwsrc

# ARP Spoof Attack Detection

def process_arp(packet):
    if packet.haslayer(ARP):
        # if it is an ARP response (ARP reply)
        if packet[ARP].op == 2:
            try:
                # get the real MAC address of the sender
                real_mac = get_mac(packet[ARP].psrc)
                # get the MAC address from the packet sent to us
                response_mac = packet[ARP].hwsrc
                # if they're different, definitely there is an attack
                if real_mac != response_mac:
                    print(f"[!] You are under attack, REAL-MAC: {real_mac.upper()}, FAKE-MAC: {response_mac.upper()}")
            except IndexError:
                # unable to find the real mac
                # may be a fake IP or firewall is blocking packets
                pass

# TCP Flood Attack Detection 
# TODO
def flow_labels(pkt):
    if IP in pkt:
        ipsrc = str(pkt[IP].src)                     # source IP
        ipdst = str(pkt[IP].dst)                     # destination IP
        try:
            sport = str(pkt[IP].sport)               # source port
            dport = str(pkt[IP].dport)               # destination port
        except:
            sport = ""
            dport = ""
        prtcl = pkt.getlayer(2).name                 # protocol

        flow = '{:<4} | {:<16} | {:<6} | {:<16} | {:<6} | '.format(prtcl, ipsrc, sport, ipdst, dport)
        # print(flow)

    # TCP SYN packet
    if TCP in pkt and pkt[TCP].flags & 2:
        src = pkt.sprintf('{IP:%IP.src%}{IPv6:%IPv6.src%}')
        syn_count[src] += 1
        if syn_count.most_common(1)[0][1] > 25 and pkt.ack == 0:
            print("Under Attack")
            attack_flag = True