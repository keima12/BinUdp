import socket
import struct
import datatype

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = datatype.TestStructure(10, 10, 1, 1, 0, 0)
client.sendto(data,("localhost",5005))
