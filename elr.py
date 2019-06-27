o=open(1,"w")
for n,c in zip(*[iter(open(0,"rb").read())]*2):o.write(chr(c)*n)