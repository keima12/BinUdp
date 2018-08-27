import socket
import struct 
import io
import datatype


"""
typedef struct {
    char identity[4];
    uint16_t x;
    uint16_t y;
} TestStructure;
"""

UDP_IP = "localhost"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
data = datatype.TestStructure()
while True:
    data1, addr = sock.recvfrom(4096)
    buffer = io.BytesIO(data1)
    buffer.readinto(data)
    print(data)
    #print(data.posi_num, data.posi_num, data.dcode, data.istat)
