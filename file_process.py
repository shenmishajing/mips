from assembler import *
f = open('bin.txt', 'r')
binary = f.read().split()
f.close()
print(type(binary))
print(binary)
'''
binary = binary.split()
for i in range(len(binary)):
    num = int(binary[i], 16)
    binary[i] = dec2bin(num, length=32)
print(binary)
'''

'''
f = open('bin.old.txt', 'w')
for b in binary:
    f.write(b + '\n')
f.close()
'''
