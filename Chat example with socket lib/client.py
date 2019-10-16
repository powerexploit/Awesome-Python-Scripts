import socket


def Main():
    host = 'localhost'
    port = 1234

    my_Socket = socket.socket()
    my_Socket.connect((host, port))

    print("Connected! {}:{}".format(host, port))

    message = input(" -> ")
    print("Waiting Server...")

    while message != 'q':
        my_Socket.send(message.encode())
        data = my_Socket.recv(1024).decode()

        print('Server: ' + data)

        message = input(" -> ")
        print("Waiting Server...")

    my_Socket.close()


if __name__ == '__main__':
    Main()