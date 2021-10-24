import socket

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        inp = input()
        s.send(inp.encode())
        data = s.recv(2048)

