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
    print(f" PORT   STATE   SERVICE")
    for port in range(1, 65536):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        try:
            result = client.connect_ex((host,port))
            if result == 0:
                service = socket.getservbyport(port)
                print(f" {port}     open    {service}")
            client.close()
        except KeyboardInterrupt:
            print("Programa finalizado!")
            sys.exit(0)
        except socket.gaierror:
            print("Hostname não pode ser resolvido.")
            sys.exit(0)
        except socket.error:
            print("Não foi possível conectar ao servidor.")
            sys.exit(0)
    return 0

def main():
    if len(sys.argv) != 2:
        print(f"Usage:\n$ ./portfinder.py example.com")
        sys.exit(1)
                                
    host = sys.argv[1]
    banner()
    port_scan(host)

if __name__ == "__main__":
    main()
