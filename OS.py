from os import *
l=listdir()
p=[]
q=[]
for i in l:
  if path.isdir(i) == True:
    p.append(i)
  else:
    q.append(i)
print(p)
print(q)
