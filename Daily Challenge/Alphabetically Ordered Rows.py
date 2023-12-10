"""

Alphabetically Ordered Rows

The program must accept a character matrix of size RxC containing only lower case alphabets as the input. The program must
print the count of rows in the matrix where the alphabets are sorted in alphabetical order as the output.

Boundary Condition(s):
2 <= R, C <= 50

Input Format:
The first line contains R and C separated by a space.
The next R lines each contain C characters separated by a space.

Output Format:
The first line contains the count of rows in the matrix where the alphabets are sorted in alphabetical order.

Example Input/Output 1:
Input:
5 4
a s d f 
h i j k
z x y q
r s t u 
u t x k

Output:
2

Explanation:
In 5x4 matrix, the alphabets in the second row and the fourth row are sorted in alphabetical order.
Second row: h i j k
Fourth row: r s t u

Hence the output is 2


Example Input/Output 2:

Input:
3 3
i j o
a z b
p c e

Output:
1


Max Execution Time Limit: 500 millisecs


Solution: Done in Python

"""

def check(a):
  c="";d=""
  b=[ord(i) for i in a]
  for i in b:
    c+=str(i)
  b.sort()
  for i in b:
    d+=str(i)
  if c==d: return 1
  else: return 0
  
a,b=map(int,input().split())
c=0
for i in range(a):
  d=list(map(str,input().split()))
  if check(d)==1: c+=1
print(c)