from pwn import *
ff = 'mysecret'
print(xor(ff, 0x55))
