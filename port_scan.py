import socket
from const import PORTAS_PRINCIPAIS

ports = PORTAS_PRINCIPAIS
host = input("Digite o endereço ip ou domínio: ")
for port in ports:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(0.1)
    code = client.connect_ex((host,port))
    if code == 0:
        print(port,"open")
