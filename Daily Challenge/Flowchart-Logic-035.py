"""

Flowchart Logic 035


Start
|
|----> Read n from input
|
|----> Set t = n, nod = 0
|
|----> While t > 0
|       |
|       |----> Increment nod by 1
|       |
|       |----> Divide t by 10
|
|----> Calculate tpv = getPow(10, n // 2)
|       |
|       |----> Set c = 1 (inside getPow function)
|       |
|       |----> While b > 0 (inside getPow function)
|       |       |
|       |       |----> Multiply c by a (inside getPow function)
|       |       |
|       |       |----> Decrement b by 1 (inside getPow function)
|
|----> Check if (n // tpv) == (n % tpv)
|       |
|       |----> If True, print "YES"
|       |
|       |----> If False, print "NO"
|
End


Sample Input/Output:

Input 1:
123123

Output 1:
YES

Input 2:
456789

Output 2:
NO

Solution: Done in Python

"""

def getPow(a, b):
  c=1
  while(b>0):
    c*=a
    b-=1
  return c

n=int(input())
t=n
nod=0
while(t>0):
  nod+=1
  t//=10
tpv=getPow(10,nod//2)
if(n//tpv==n%tpv):
  print("YES")
else:
  print("NO")
