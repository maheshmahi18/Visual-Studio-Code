"""

Vertically Downward Asterisks Pattern

The program must accept a list of integers as the input. The program must print the desired pattern as shown in the Example
Input/Output section.

Boundary Condition(s):
1 <= Each integer value <= 100

Input Format:
The first line contains the list of integers.

Output Format:
The lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:

Input:
5 6 1 4 2

Output:
*****
**-**
**-*-
**-*-
**---
-*---


Example Input/Output 2:

Input:
7 3 4 5

Output:
****
****
****
*-**
*--*
*---
*---


Max Execution Time Limit: 500 millisecs

Solution: Done in Python


"""

n=list(map(int,input().split()))
a=[]
for i in range(len(n)):
    b=""
    for j in range(1,max(n)+1):
        if(n[i]>=j): b+='*'
        else: b+='-'
    a.append(b)
for i in range(max(n)):
    for j in range(len(n)):
        print(a[j][i],end="")
    print()