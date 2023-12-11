"""

Sum - Ending with X

The program must accept N integers and an integer X as the input. The program must print the sum of integers ending with X among the N integers as the output. If there is no such integer, the program must print 0 as the output.

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 10^7

Input Format:
The first line contains N and X separated by a space.
The second line contains N integers separated by a space.

Output Format:
The first line contains the sum of integers ending with X among the N integers.

Example Input/Output 1:

Input:
5 4
87 54 15 984 104

Output:
1142

Explanation:
The integers ending with 4 among the 5 integers are 54, 984 and 104.

Hence their sum 1142 (54 + 984 + 104) is printed as the output.

Example Input/Output 2:

Input:
4 87
187 95787 154 978

Output:
95974

Example Input/Output 3:

Input:
6 400
6500 98 2 540 12 14

Output:
0

Max Execution Time Limit: 1000 millisecs


Solution: Done in Python

"""

a,b=map(str,input().split())
c=list(map(str,input().split()))
d=[int(i) for i in c if i[-len(b):]==b]
print(sum(d))