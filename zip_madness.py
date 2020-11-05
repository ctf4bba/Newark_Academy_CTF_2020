# coding: utf-8
import zipfile

with zipfile.ZipFile('flag.zip') as z:
    z.extractall()

for i in range(1000, 0, -1):
    with open('direction.txt') as d:
        di = d.read()

    filename = str(i) + di.strip() + '.zip'
    with zipfile.ZipFile(filename) as z:
        z.extractall()
        
