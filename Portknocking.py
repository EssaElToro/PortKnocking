import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
def connect_and_send(p):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('IP',p)) # w nawias wpisujemy IP
    s.sendall(b'xD')
    s.close()

for p1 in range(8000,8100): #w nawiasy wpisujemy zakres portow
    for p2 in range(8000,8100): # --||--
        for p3 in range(8000,8100): # --||--

            connect_and_send(p1)
            connect_and_send(p2)
            connect_and_send(p3)

            connect_and_send(p1)
            connect_and_send(p2)
            connect_and_send(p3)

            print(p1, p2, p3)
