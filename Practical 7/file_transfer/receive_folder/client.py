import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Please enter the host address of the sender : ")
port = 8080
client.connect((host, port))
print("Connected to the server ! ")
filename = input("Enter the filename you want to save in : ")
host.send(filename.encode('utf-8'))

file = open(filename, 'wb')
file_data = client.recv(2048)
file.write(file_data)
file.close()
print("file received ..... ")
