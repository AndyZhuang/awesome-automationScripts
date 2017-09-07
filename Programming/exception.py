import socket
socket.setdefaulttimeout(2)
s = socket.socket()
try:
    s.connect(("127.0.0.1",9050))
except Exception, e:
    print "[-] the Error " + str(e)
