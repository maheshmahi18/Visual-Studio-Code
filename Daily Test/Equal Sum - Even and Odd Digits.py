"""

Equal Sum - Even and Odd Digits

The program must accept an integer N as the input. The program must print the values from 1 to N where the sum of odd digits is equal to the sum of even digits as the output.

Boundary Condition(s):
112 <= N <= 10^5

Input Format:
The first line contains N.

Output Format:
The first line contains the values based on the given condition.

Example Input/Output 1:

Input:
160

Output:
112 121 134 143 156

Explanation:
In the first integer 112, the sum of odd digits is 2 (1+1) and the sum of even digit is 2 (2). So 112 is printed.
In the second integer 121, the sum of odd digits is 2 (1+1) and the sum of even digit is 2 (2). So 121 is printed.
In the third integer 134, the sum of odd digits is 4 (1+3) and the sum of even digit is 4 (4). So 134 is printed.
In the fourth integer 143, the sum of odd digits is 4 (1+3) and the sum of even digit is 4 (4). So 143 is printed.
In the fifth integer 156, the sum of odd digits is 6 (I +5) and the sum of even digit is 6 (6). 
So 156 is printed.

All integers other than 112 121 134 143 156 from 1 to 160 are not printed because they do not meet the given conditions.

Example Input/Output 2:

Input:
500

Output:
112 121 134 143 156 165 178 187 211 314 336 341 358 363 385 413 431

Solution: Done in Python

"""

n=int(input())
a=[]
for i in range(1,n+1):
    b=[];c=[]
    for j in str(i):
        if(int(j)%2==0): b.append(int(j))
        else: c.append(int(j))
    if(sum(b)==sum(c)): a.append(i)
print(*a)