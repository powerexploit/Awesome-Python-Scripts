import socket
import time


def Main():
    host = "localhost"
    port = 1234

    my_Socket = socket.socket()
    my_Socket.bind((host, port))

    my_Socket.listen(1)
    conn, addr = my_Socket.accept()
    print("Connection from: " + str(addr))
    while True:
        while True: # this line, if the client closed the connection, it waits for new connections.
            try:
                data = str(conn.recv(1024).decode())
                print("Client: " + data)
                break
            except ConnectionResetError:
                time.sleep(1)
                conn, addr = my_Socket.accept()
                print("Connection from: " + str(addr))
        if data == "q":
            break
        else:
            message = input(" -> ")
            print("Waiting Client...")
            conn.send(message.encode())
    conn.close()


if __name__ == '__main__':
    Main()