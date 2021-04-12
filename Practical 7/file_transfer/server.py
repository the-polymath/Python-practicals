import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080

server.bind((host, port))
server.listen(1)

print(host)
print("Waiting for any incoming connections ...... ")

client, address = server.accept()
print(f'{client}, {address} has connected to the server ! ')

filename = input("Enter the filename you want to send : ")
print(f'Reading {filename} ........')
file = open(filename, 'rb')
file_data = file.read(2048)
client.send(file_data)
file.close()
print("data has been tranmitted successfully ......")
