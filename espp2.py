from pwn import *
p = remote("ctf.sentinel-cyber.sg", 32029)
p.sendline("START")
p.sendline("USERNAME|john")
p.recvuntil("CHALLENGE|")
chall = int(p.recvuntil("\n").decode())
resp = chall ^ 0x41A9CC23
p.sendline(f"RESPONSE|{resp}")
p.interactive()