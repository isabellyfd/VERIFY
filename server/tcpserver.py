import socket
import sys

# Create a TCP/IP socket
sockrecv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, 'connection from', client_address

        data = NULL
        # Receive the data in small chunks and retransmit it
        while True:
            data = data+connection.recv(16000)
            if len(data) > 71400:
                break             

        f = open("teste.mp4", "w")
        f.write(data)
        f.close()
            
    finally:
        # Clean up the connection
        connection.close()
