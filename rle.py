import sys as s
import itertools as t
x=s.stdin.buffer.read()
o=s.stdout
if '-d'in s.argv:
 for n,c in zip(*[iter(x)]*2):
  o.write(chr(c)*n)
else:
 for c,g in t.groupby(x):
  q,r=divmod(len([*g]),255)
  o.buffer.write(bytes([*[255,c]*q,r,c]))