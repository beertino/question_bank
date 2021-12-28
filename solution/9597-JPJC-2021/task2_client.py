import socket
client_socket = socket.socket()

address = input('Enter IPv4 address of server: ')
port = int(input('Enter port number of server: '))

client_socket.connect((address, port))

while True:
    data = client_socket.recv(1024)
    if b"Enter" in data:
        choice = input(data.decode())
        client_socket.sendall(choice.encode())
    else:
        print(data.decode())
        if b"GAME OVER..." in data or b"YOU WON" in data:
            break

print('Game has ended. Please reconnect to play again')

client_socket.close()