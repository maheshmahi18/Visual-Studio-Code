"""

String X - Pattern

The program must accept a string S as the input. The program must print the desired pattern as shown in the Example
Input/Output section.

Boundary Condition(s):
3 <= Length of S <= 50

Input Format:
The first line contains S.

Output Format:
The lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:

Input:
water

Output:
w * * * a
* t * e *
* * r * *
* t * e * 
w * * * a


Example Input/Output 2:

Input:
OFFICE

Output:
O * * * * F
* F * * I *
* * C E * *
* * C E * *
* F * * I *
O * * * * F


Max Execution Time Limit: 500 millisecs

Solution: Done in Python


"""

s=input().strip()
a=s[::2]+s[1::2][::-1]
for i in range(len(a)):
    for j in range(len(a)):
        if(i==j): print(a[i],end=" ")
        elif(i+j==len(a)-1): print(a[j],end=" ")
        else: print("*",end=" ")
    print()