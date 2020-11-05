# coding: utf-8
import collections
with open('enc.txt', 'r') as f:
    enc = f.read()

line = ''
for i in range(0, len(enc), 8):
    line += chr(int(enc[i:i+8], 2))

l = []
for i in range(0, len(line), 29):
    l.append(line[i:i+29])

flag = ''
for i in range(len(l[0])):
    tmp_l = []
    for j in range(len(l)):
        tmp_l.append(l[j][i])
    c = collections.Counter(tmp_l)
    flag += c.most_common()[0][0]

print(flag)