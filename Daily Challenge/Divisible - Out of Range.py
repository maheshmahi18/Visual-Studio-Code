"""

Divisible - Out of Range

The program must accept three integers X, Y and Z as the input. The program must find and print the smallest positive integer
N based on the following conditions.
- N is divisible by Z.
- N is not equal to any of the integers from X to Y (where X < Y).

Boundary Condition(s):
1 <= X,Y,Z <= 10^8

Input Format:
The first line contains X, Y and Z separated by a space.

Output Format:
The first line contains N.


Example Input/Output 1:

Input:
2 8 2

Output:
10

Explanation:
10 is the smallest integer which is divisible by 2 and it is not equal to any integers from 2 to 8.

So 10 is printed as the output.


Example Input/Output 2:

Input:
5 10 4

Output:
4


Max Execution Time Limit: 1000 millisecs


Solution: Done in Python


"""
x,y,z=map(int,input().split())
a=z
while(a>=x and a<=y):
    a+=z
print(a)