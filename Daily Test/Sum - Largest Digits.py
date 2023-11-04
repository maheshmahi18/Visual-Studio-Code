"""

Sum - Largest Digits

The program must accept N integers as the input. The program must print the sum of the largest digit in each integer among the N integers as the output.

Boundary Condition(s):

2 <= N <= 1000
O <= Each integer value <= 10^4

Input Format:
The first line contains
The second line contains N integers separated by a space.

Output Format:
The first line contains the sum of the largest digit in each integer among the N integers.

Example Input/Output 1:

Input
5
87 1654 121 657 15

Output:
28

Explanation:

The largest digit in 87 is 8,
The largest digit in 1654 is 6.
The largest digit in 121 is 2.
The largest digit in 657 is 7.
The largest digit in 15 is 5.
So the sum of each largest digit is 28 (8+6+2+7+5),

Hence the output is 28

Example Input/Output 2:

Input
4
0 444 10 25

Output:
10

Sollution: Done in Python


"""

n=int(input())
a=list(map(str,input().split()))
b=[]
for i in a:
    c=[int(j) for j in i]
    b.append(max(c))
print(sum(b))