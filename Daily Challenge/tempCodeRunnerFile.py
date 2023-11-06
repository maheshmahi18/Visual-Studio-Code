def getPow(a,b):
  c=1
  while(b>0):
    c*=a
    b-=1
n=int(input())
t=n
nod=0
while(t>0):
  nod+=1
  t//=10
  tpv=getPow(10,n//2)
if(n//tpv==n%tpv): print("YES")
else: print("NO")