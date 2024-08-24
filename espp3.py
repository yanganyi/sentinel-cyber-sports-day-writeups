from pwn import *

USERS_DB = {
'larry' : 0x496c6b43,
'bridget' : 0xf60977a6,
'billy' : 0x7e337272,
'peter' : 0xe8fbbcbe,
'donald' : 0x14107096,
'hilda' : 0xae1782a5,
'javier' : 0xf623bd34,
'juan' : 0x40ea256f,
'john' : 0xd8177179,
'carolyn' : 0x49559a18,
'jonathan' : 0x58478709,
'martin' : 0xea8e66ad,
'donna' : 0xfdf44767,
'helen' : 0xa4a9c387,
'michael' : 0x9b6baafd,
'velma' : 0x1758ade5,
'linda' : 0xee04ecb3,
'belinda' : 0x689c228d,
'tammy' : 0xeced5f47,
'florida' : 0x327f4716,
'ernest': 0xf93ac6de,
'debra': 0x3d20d707,
'freddie': 0x0c8e88bf,
'martha': 0x3d34adae,
'carol': 0xa3e664d1,
'patricia': 0xf4c66b2b,
'mattie': 0x88e9710a,
'samuel': 0xfe8b33f5,
'melissa': 0xbf9f24c4,
'charles': 0x0e28a0a2,
'jill': 0x5dd3ee0e,
'william': 0xa56ffef9,
'edith': 0x87b851cc,
'dawn': 0x41e2d253,
'scott': 0xcae427c8,
'raymond': 0x2f492ec1,
'robert': 0x037f1270,
'rudy': 0xe6b1d19b,
'meg': 0x852e7a7d,
'frederick': 0x35de9ab1,
'tyler': 0x01580988,
'david': 0x63814141,
'bill': 0x1330d34f,
'todd': 0x1378b9e0,
'thomas': 0xd634a520,
'graciela': 0x9d2fe22f,
'shelly': 0x8adc1f88,
'valerie': 0xf470de7d,
'kenneth': 0x504e3a64,
'jessica': 0x9be8620a,
}

for user in USERS_DB.keys():
    p = remote("ctf.sentinel-cyber.sg", 42915)
    p.sendline("START")
    print(user, USERS_DB[user])
    p.sendline(f"USERNAME|{user}")
    p.recvuntil("CHALLENGE|")
    challenge = int(p.recvuntil('\n').decode())
    response = challenge ^ USERS_DB[user]
    response += sum([ord(c) for c in user])
    p.sendline(f"RESPONSE|{response}")
    print(p.recv())
    p.close()