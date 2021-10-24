import socket
import os

if __name__ == '__main__':

    HOST = 'localhost'
    PORT = 65432
    os.chdir('serverfile')
    with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            while True:
                filename = conn.recv(1024).decode()
                if (filename in os.listdir()):
                    msg = "OK, 200"
                    conn.sendall(msg.encode())
                    html_content = ''
                    with open(filename, 'r') as reader:
                        for line in reader.readlines():
                            html_content += line
                    conn.sendall(html_content.encode())
                else:
                    msg = "404, Not Found"
                    conn.sendall(msg.encode())
                    break