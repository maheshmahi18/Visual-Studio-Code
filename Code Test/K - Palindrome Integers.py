"""

K - Palindrome Integers


The program must accept two integers N and K as the input. The program must print the first K palindromic integers greater
than N as the output.

Boundary Condition(s):
1 <=N <= 10^7
1 <= K <= 1000

Input Format:
The first line contains N and K separated by a space.

Output Format:
The first line contains K integers representing the first K palindromic integers greater than N.

Example Input/Output 1:

Input:
1221 5

Output:
1331 1441 1551 1661 1771

Explanation:
Here N = 1221 and 5.
The first 5 palindromic integers greater than 1221 are 1331, 1441, 1551, 1661 and 1771.

Hence the output is
1331 1441 1551 1661 1771

Example Input/Output 2:

Input:
658100 10

Output:
658856 659956 660066 661166 662266 663366 664466 665566 666666 667766


Sollution: Done in Python


"""
def check(n):
    return str(n)==str(n)[::-1]   
a,b=map(int,input().split())
c=[]
d=a+1
while(len(c)<b):
    if check(d):
        c.append(d)
    d+=1
print(*c)