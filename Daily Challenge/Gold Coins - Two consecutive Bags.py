"""

Gold Coins - Two consecutive Bags

There are five bags in a row where each bag contains gold coins. The number of gold coins in each bag is passed as the input. The program must print the maximum number of gold coins by choosing any two consecutive bags as the output.

Boundary Condition(s):
0 <= Each integer value <= 10^4

Input Format:
The first line contains five integers separated by a space.

Output Format:
The first line contains the maximum number of gold coins by choosing any two consecutive bags.

Example Input/Output 1:

Input:
1 2 3 4 5

Output:
9

Explanation:
Bags 1 and 2 have 1+2 = 3 gold coins.
Bags 2 and 3 have 2+3 = 5 gold coins.
Bags 3 and 4 have 3+4 = 7 gold coins.
Bags 4 and 5 have 4+5 = 9 gold coins.

The maximum number of gold coins 9 is obtained by choosing the bags 4 and 5.


Example Input/Output 2:

Input:
9 0 8 4 1

Output:
12


Max Execution Time Limit: 1000 millisecs


Sollution: Done in Python

"""

n=list(map(int,input().split()))
b=[n[i]+n[i+1] for i in range(len(n)-1)]
print(max(b))