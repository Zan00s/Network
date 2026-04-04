from scapy.all import *

def send_packet():
    packet = IP(dst="127.0.0.1", src="127.0.0.1") / TCP(dport=12345, sport=12345) / Raw(b"Dear Steel Cat! This is no attack, it's my humster Pinkie you should track")
    
    send(packet)

if __name__ == "__main__":
    send_packet()
