#!/usr/bin/python3

import socket
import sys

def banner():
        print(r" ____            _   _____ _           _           ")
        print(r"|  _ \ ___  _ __| |_|  ___(_)_ __   __| | ___ _ __ ")
        print(r"| |_) / _ \| '__| __| |_  | | '_ \ / _` |/ _ \ '__|")
        print(r"|  __/ (_) | |  | |_|  _| | | | | | (_| |  __/ |   ")
        print(r"|_|   \___/|_|   \__|_|   |_|_| |_|\__,_|\___|_|   ")
        print(f"Created by @7acini\n")
        

def port_scan(host):
    print(f" PORT   STATE")
    for port in range(1, 5000):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.05)
        if client.connect_ex((host,port)) == 0:
            print(f" {port}     open")
    return 0

def main():
    banner()
    try:
        port_scan(sys.argv[1])    
    except IndexError:
        print(f"Usage:\n$ ./portfinder example.com")
        sys.exit(0)

main()

