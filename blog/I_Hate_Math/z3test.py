#coding:utf-8
'''
	@DateTime: 	2017-11-27 15:32:20
	@Version: 	1.0
	@Author: 	Unname_Bao
'''
from z3 import *
import time
t1 = time.time()
solver = Solver()
flag = [Int('flag%d'%i) for i in range(36)]
a = [i for i in flag]
b = [i for i in range(36)]
c = [0 for i in range(36)]
d = [0x12027,0x0F296,0x0BF0E,0x0D84C,0x91D8,0x297,0x0F296,0x0D830,0x0A326,0x0B010,0x7627,0x230,0x0BF0E,0x0A326,0x8FEB,0x879D,0x70C3,0x1BD,0x0D84C,0x0B010,0x879D,0x0B00D,0x6E4F,0x1F7,0x91D8,0x7627,0x70C3,0x6E4F,0x9BDC,0x15C,0x297,0x230,0x1BD,0x1F7,0x15C,0x6]
for i in range(6):
	for j in range(6):
		b[i+6*j] = a[6*i+j]
for i in range(6):
	for j in range(6):
		for k in range(6):
			c[j+6*i] = c[j+6*i] + a[6*i+k]*b[6*k+j]
		solver.add(simplify(c[j+6*i]) == d[j+6*i])
for i in range(6,36-10):
	solver.add(flag[i]>=32)
	solver.add(flag[i]<=127)
for i in range(6):
	solver.add(flag[i] == ord('whctf{'[i]))
for i in range(36-9,36):
	solver.add(flag[i] == 0x1)
solver.add(flag[-10] == ord('}'))
if solver.check() == sat:
	m = solver.model()
	s = []
	for i in range(36):
		s.append(m[flag[i]].as_long())
	print(bytes(s))
else:
	print('error')
t2 = time.time()
print(t2-t1)
