import socket

HOST = '127.0.0.1'
PORT = 8000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

dados = []

while True:
    data = client.recv(1024)

    if not data:
        break

    dados.append(data)

print(dados[-1].decode())

client.close()
