"""

Sum of N Modified Integers

The program must accept N integers as the input. For each even integer X among the N integers, the program must
double the integer X. For each odd integer Y among the N integers, the program must quadruple the integer Y. Then the
program must print the sum of N modified integers as the output.

Boundary Condition(s):
1 <= N <= 1000
1 <= Each integer value <= 1000

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the sum as per the given conditions.

Example Input/Output 1:

Input:
4
5 2 8 7

Output:
68

Explanation:
Here N = 4.
The first integer 5 is odd, so 5*4 = 20.
The second integer 2 is even, so 2*2 = 4.
The third integer 8 is even, so 8*2 = 16.
The fourth integer 7 is odd, so 7*4 = 28.

So their sum 68 is printed as the output.


Example Input/Output 2:

Input:
5
4 9 1 1 8

Output:
68

Max Execution Time Limit: 1000 millisecs


Solution: Done in Python


"""

n=int(input())
a=list(map(int,input().split()))
b=[i*2 if i%2==0 else i*4 for i in a]
print(sum(b))