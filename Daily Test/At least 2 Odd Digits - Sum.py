"""

At least 2 Odd Digits - Sum

The program must accept N integers as the input. The program must print the sum of integers containing at least two odd digits among the N 
integers as the output.

Boundary Condition(s):
1 <= N <= 10^4
1 <= Each integer value <= 10^4

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the sum of integers containing at least two odd digits.

Example Input/Output 1:

Input:
5
78 549 123 877 214

Output:
1549

Explanation:

In the given 5 integers, 549 123 and 877 are having at least 2 odd digits.
So the sum of those integers is 1549.

Hence the output is 1549

Example Input/Output 2:

Input:
4
124 4266 184 42

Output:
0


Sollution: Done in Python


"""

n=int(input())
a=list(map(int,input().split()))
b=[]
for i in a:
    c=0
    for j in str(i):
        if int(j)%2!=0: c+=1
    if(c>=2): b.append(i)
print(sum(b))