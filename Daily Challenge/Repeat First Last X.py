"""

Repeat First/Last X

The program must accept two integers N and X as the input. The program must print the integers from 1 to N based on the following conditions.

- If X is a positive integer then repeat the first X integers twice among the integers from 1 to N.
- If X is a negative integer then repeat the last X integers twice among the integers from 1 to N.

Note: The value of X is always non-zero.

Boundary Condition(s):
1 <= N <= 1000
-N <= X <= N
Input Format:
The first line contains N and X separated by a space.

Output Format:
The first line contains a list of integers separated by a space as per the given conditions.


Example Input/Output 1:

Input:
10 5

Output:
1 1 2 2 3 3 4 4 5 5 6 7 8 9 10

Explanation:
Here is X = 5, which is a positive integer.
So the first 5 integers are repeated twice from 1 to 10.
Hence the output is 1 1 2 2 3 3 4 4 5 5 6 7 8 9 10


Example Input/Output 2:

Input:
10 -5

Output:
1 2 3 4 5 6 6 7 7 8 8 9 9 10 10


Example Input/Output 3:

Input:
13 -2

Output:
1 2 3 4 5 6 7 8 9 10 11 12 12 13 13


Max Execution Time Limit: 1000 millisecs


Solution: Done in Python

s
"""