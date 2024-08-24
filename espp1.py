from pwn import *
p = remote("ctf.sentinel-cyber.sg", 1337)
p.sendline("START")
p.sendline("USERNAME|john")
chall = int(p.recvuntil("\n").decode())
p.interactive()