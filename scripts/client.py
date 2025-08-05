import socket
import time

import bufsock

#give the server a second to start up
time.sleep(10)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("127.0.0.1", 4444))
bs = bufsock.bufsock(s)

while True:
    #read the prompt in and print it
    data = bs.readto(b'\n')
    print(data)

    #read command from the user terminal
    cmd = input()

    # send the command to the server
    bs.send(cmd.encode('utf-8'))
    bs.send(b'\n')
    bs.flush()

    data = bs.readto(b'\n')
    print(data)
    
