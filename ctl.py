#!/usr/bin/env python3
""" ctl for connecting to and sending data into Unix Socket
"""

from socket import AF_UNIX, SOCK_STREAM, socket
from sys    import argv

if __name__ == "__main__":
    msg = " ".join( argv[ 1: ] )
    socket_name = "foobar.sock"
    with socket( AF_UNIX , SOCK_STREAM ) as sock:
        sock.connect( socket_name )
        sock.sendall( msg.encode() )