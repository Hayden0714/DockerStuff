import socket
import time

import bufsock

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind(("0.0.0.0", 4444))
s.listen(1)

while True:
    connexion, client_address = s.accept()

    print("connexion from: " + str(client_address))
    bs = bufsock.bufsock(connexion)

    while True:
        bs.send(b"Enter cmd: \n")
        bs.flush()
        cmd = bs.readto(b'\n').rstrip(b'\n')
        if cmd == b'TIME':
            result = time.ctime().encode('utf-8')
            bs.send(result)
        else:
            bs.send(b'Unrecognized command: %s' % (cmd, ))
        bs.send(b'\n')
        bs.flush()