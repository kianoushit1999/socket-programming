import socket

if __name__ == '__main__':

    HOST = 'localhost'
    PORT = 65432

    with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if data == 'end':
                    break
                conn.sendall(data.decode().capitalize().encode())