import socket
from p2p_functions.p2p_listen import start_listening
from p2p_functions.p2p_transfer import bind_socket
UDP_IP = "0.0.0.0"  # ready for all
UDP_PORT = 4444
print("welcome to p2p\n"
      "commands: \n"
      "‫‪p2p‬‬ ‫‪–receive‬‬ <file_name>\n"
      "‫‪p2p‬‬ ‫‪–serve‬‬ ‫‪-name‬‬ <file_name>‬‬ ‫‪-path‬‬ <file_path>\n‫‬‬‬‬")

hostname = socket.gethostname()
COMMUNICATION_PORT = 4444
TRANSFER_PORT = 3333
files = []
print("Host ", hostname, " joined in port ", COMMUNICATION_PORT)
start_listening(bind_socket(COMMUNICATION_PORT),files,hostname,TRANSFER_PORT)
print("hello")