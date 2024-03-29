"""

Largest Possible - Concatenate Two Integers

The program must accept three integers X. Y and Z as the input. The program must print the largest possible integer which is obtained by concatenating any two integers among X, Y and Z as the output

Boundary Condition(s):
O <= X,Y,Z <= 10^5

Format:
The first line contains X, Y and Z.

Output Format:
The first line contains an integer based on the given condition.

Example Input/Output 1:

Input
100 2 10

Output:
10100

Explanation:

The largest possible integer 10100 is obtained by concatenating the integers 10 and 100.

Hence the output is 10100

Example Input/Output 2:

Input
45 81 12

Output:
8145

Example Input/Output 3:

Input
0 2 5

Output:
52


Sollution: Done in Python

"""

a,b,c=map(int,input().split())
d=[a,b,c]
d.sort(reverse=True)
m=str(d[1]);n=str(d[0])
e=[int(m+n),int(n+m)]
print(max(e))