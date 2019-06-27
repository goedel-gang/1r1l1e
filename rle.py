from itertools import*
o=open(1,"wb")
for c,g in groupby(open(0,"rb").read()):q,r=divmod(len([*g]),255);o.write(bytes([*[255,c]*q,r,c]))