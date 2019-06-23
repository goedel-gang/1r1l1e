from sys import*
from itertools import*
x=stdin.buffer.read()
o=stdout
if '-d'in argv:
 for n,c in zip(*[iter(x)]*2):
  o.write(chr(c)*n)
else:
 for c,g in groupby(x):
  q,r=divmod(len([*g]),255)
  o.buffer.write(bytes([*[255,c]*q,r,c]))