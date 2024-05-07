#!/usr/bin/env python3 
import logging
from scapy.all import *
import argparse

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def spoof_syn_ack(packet):
    if TCP in packet and packet[TCP].flags == 'S':
        src_ip = packet[IP].dst
        dst_ip = packet[IP].src
        src_port = packet[TCP].dport
        dst_port = packet[TCP].sport

        ip = IP(src=src_ip, dst=dst_ip)
        tcp = TCP(sport=src_port, dport=dst_port, flags='SA', seq=1000, ack=packet[TCP].seq + 1)
        send(ip/tcp, verbose=0)
        logging.info(f"Sent SYN+ACK from {src_ip}:{src_port} to {dst_ip}:{dst_port}")

def main():
    parser = argparse.ArgumentParser(description="A robust TCP SYN-ACK spoofer")
    parser.add_argument("--port", type=int, help="Specify a single port to protect")
    args = parser.parse_args()

    filter_rule = "tcp"
    if args.port:
        filter_rule += f" and port {args.port}"

    logging.info("Starting to sniff. Ctrl+C to stop.")
    sniff(prn=spoof_syn_ack, filter=filter_rule, store=0)

if __name__ == "__main__":
    main()
