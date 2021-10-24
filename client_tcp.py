import socket

if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 65432

    with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        inp = input("Enter your content")
        client.sendall(inp.encode())
        data = client.recv(2048)
        print(data.decode())
