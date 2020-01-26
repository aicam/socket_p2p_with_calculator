import socket
from p2p_functions.p2p_listen import start_listening
from p2p_functions.socket_binds import *
from p2p_functions.p2p_receive import ask_for_file
import random

print("welcome to p2p\n"
      "commands: \n"
      "‫‪p2p‬‬ ‫‪–receive‬‬ <file_name>\n"
      "‫‪p2p‬‬ ‫‪–serve‬‬ ‫‪-name‬‬ <file_name>‬‬ ‫‪-path‬‬ <file_path>\n‫‬‬‬‬")

hostname = socket.gethostname() + str(random.randint(100,1000))
COMMUNICATION_PORT = 3001
TRANSFER_PORT = 3002
files = []
communication_socket = bind_socket_server(COMMUNICATION_PORT)
transfer_socket = bind_socket_server(TRANSFER_PORT)
stop_thread = False
print("Host ", hostname, " joined in port ", COMMUNICATION_PORT)
listener = start_listening(communication_socket, transfer_socket, files, hostname, COMMUNICATION_PORT, TRANSFER_PORT)
listener.start()
command = input('enter command : ')
while command.rstrip() != "FINISHED":
      command_args = command.rstrip().split(' ')
      if command.__contains__('serve'):
            files.append({'name': command_args[3].rstrip(), 'path': command_args[5].rstrip()})
            print('file added successfully\n')
      if command.__contains__('receive'):
            ask_for_file(communication_socket, transfer_socket, command_args[2], bind_socket_client(), COMMUNICATION_PORT, TRANSFER_PORT, hostname)
      command = input('enter command : ')
print("hello")
