import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
# Now you have socket connected to the web server

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode(
)  # this is a request
mysock.send(cmd)

while True:  #run until we meet the end of the loop
    data = mysock.recv(
        1024
    )  #receive up to 512 characters but have wired chunk here so i changed it into 1024
    if (len(data) < 1):  # when you meet the end of the file
        break
    print(data.decode())
mysock.close()
