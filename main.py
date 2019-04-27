from assembler import *
import wx
from main_form import MainFrame

'''
for i in range(32):
    s = 'R' + str(i)
    print(find_register(s))

print()

for i in range(32):
    s = 'r' + str(i)
    print(find_register(s))

print()

print(find_register('zero'))
for i in range(2):
    s = 'v' + str(i)
    print(find_register(s))
for i in range(4):
    s = 'a' + str(i)
    print(find_register(s))
for i in range(8):
    s = 't' + str(i)
    print(find_register(s))
for i in range(8):
    s = 's' + str(i)
    print(find_register(s))
for i in range(8, 10):
    s = 't' + str(i)
    print(find_register(s))
print(find_register('gp'))
print(find_register('sp'))
print(find_register('fp'))
print(find_register('ra'))

print()

for i in range(32):
    print(find_register(i))
    
'''

'''

f = open('bin.txt', 'r')
binary = f.read().split()
f.close()
print(type(binary))
print(binary)

code = inv_assembler(binary)
print(code)

f = open('code.txt', 'w')
for c in code:
    f.write(c + '\n')
f.close()

'''

app = wx.App()
main_frame = MainFrame(None)
main_frame.Show()
app.MainLoop()

'''
f = open('code.txt', 'r')
code = f.read().split('\n')
f.close()
print(type(code))
print(code)

binary = assembler(code)
print(binary)

f = open('bin.txt', 'w')
for b in binary:
    f.write(b + '\n')
f.close()
'''
