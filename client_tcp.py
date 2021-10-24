import socket

if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 65432

    with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))

        file_name = input("Enter your content: \n")
        saved_addr = input("Enter your address(for save): \n")

        client.sendall(file_name.encode())
        while(True):
            data = client.recv(2048)
            if ("ok" not in data.decode()):
                print("404, Not found")
            html_content = client.recv(4096)
            with open(saved_addr, 'w') as writer:
                writer.write(html_content.decode())