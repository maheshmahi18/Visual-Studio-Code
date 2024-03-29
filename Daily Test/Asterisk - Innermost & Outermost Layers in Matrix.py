"""

Asterisk - Innermost & Outermost Layers in Matrix

The program must accept a character matrix of size NXN containing only alphabets as the input. The program must replace the
innermost layer and the outermost layer of the matrix by the asterisk Then the program must print the modified matrix as the
output

Boundary Condition(s):
3 <= N <= 100

Input Format:
The first line contains N.
The next N lines each contain N alphabets separated by a space.

Output Format
The first N lines containing the modified matrix.


Example Input/Output 1:
Input:
5
d z y w y
y k h a j
z y b w l
w i n t w
e r t y u

Output:
* * * * *
* k h a *
* y * w *
* i n t *
* * * * *

Explanation:
In the given 5x5 matrix, the inn«most lay« and the layer are highlighted below.
After replacing the innermost layer and the outermost layer of the matrix by the asterisk.


Example Input/Output 2:

Input:
8
U A L K Y A N V
S I U G D T A Z
D T B J P D C A
U Z S T Q H O C
A Q C U R M M C
D R A T B O T J
X X S R D T P M
F Z F E O C G A

Output:
* * * * * * * *
* I U G D T A *
* T B J P D C *
* Z S * * H O *
* Q C * * M M *
* R A T B O T *
* X S R D T P *
* * * * * * * *


Example Input/Output 3:

Input:
4
h x b l
u q l v
y c y o
e m a c

Output:
* * * *
* * * *
* * * *
* * * *

Solution: Done in Python

"""

n=int(input())
a=[]
for i in range(n):
  a.append(list(map(str,input().split())))
if(n%2==0):
  for i in range(n):
    for j in range(n):
      if((i==n//2 and j==n//2) or (i==n//2 and j==n//2-1) or (i==n//2-1 and j==n//2) or (i==n//2-1 and j==n//2-1) or i==0 or i==n-1 or j==0 or j==n-1): print("*",end=" ")
      else: print(a[i][j],end=" ")
    print()
else:
  for i in range(n):
    for j in range(n):
      if((i==n//2 and j==n//2) or i==0 or i==n-1 or j==0 or j==n-1): print("*",end=" ")
      else: print(a[i][j],end=" ")
    print()