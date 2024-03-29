""""
Swap - Every Two Odd Integers

The program must accept N integers as the input. The program must swap every two odd integers in their positions among the
N integers. The program must print the revised values of N integers as the output. If the number of odd integers in the given N
integers is odd then the program must keep that last odd integer as it is.

Boundary Condition(s):
2 <= N <= 1000
1 <= Each integer value <= 10^5

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the revised values of N integers separated by a space.

Example Input/Output 1:

Input:
7
22 23 51 56 69 53 29

Output:
22 51 23 56 53 69 29

Explanation:
After swapping the first two odd integers 23 and 51 in the given 7 integers, the integers become 22 51 23 56 69 53 29.
After swapping the last two odd integers 69 and 53 in the given 7 integers, the integers become 22 51 23 56 53 69 29.

Hence the output is 22 51 23 56 53 69 29


Example Input/Output 2:

Input:
5
3 4 7 21 89

Output:
7 4 3 89 21

Max Execution Time Limit: 500 millisecs


Solution: Done in Python


"""
def rev(a):
  b=[];c=0;d=1
  for i in range(len(a)//2):
    b.append(a[1])
    b.append(a[0])
    a.remove(a[1])
    a.remove(a[0])
  if len(a)>=1:
    b.append(*a)
  return b

n=int(input())
a=list(map(int,input().split()))
b=[i for i in a if i%2==1]
c=rev(b)
d=0
for i in a:
  if(i%2==1): print(c[d],end=" "); d+=1
  else: print(i,end=" ")