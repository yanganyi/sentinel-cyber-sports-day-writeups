import socket
import struct

SERVER_HOST = "ctf.sentinel-cyber.sg"
SERVER_PORT = 52122

CMD_2 = b'\x20'
ARG_TYPE_1 = b'\x61'
ARG_TYPE_2 = b'\x62'

def send_command(sock, cmd, args):
    sock.send(cmd)
    sock.send(struct.pack('B', len(args)))
    for arg in args:
        if isinstance(arg, str):
            sock.send(ARG_TYPE_1)
            sock.send(struct.pack('<H', len(arg)))
            sock.send(arg.encode())
        elif isinstance(arg, int):
            sock.send(ARG_TYPE_2)
            sock.send(struct.pack('<I', arg))

def receive_response(sock):
    status = sock.recv(1)
    if status != b'\xEE':
        print(f"Error: Received status {status}")
        return None
    
    length = struct.unpack('<I', sock.recv(4))[0]
    return sock.recv(length)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_HOST, SERVER_PORT))

try:
    filename = "flag.txt"
    bytes_to_read = 100
    send_command(sock, CMD_2, [filename, bytes_to_read])

    response = receive_response(sock)
    if response:
        print(f"Received data: {response}")
    else:
        print("Failed to receive data")

finally:
    sock.close()