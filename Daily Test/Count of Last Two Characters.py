"""

Count of Last Two Characters

The program must accept a string S as the input. The program must find and print the number of occurrences of the last two
characters of S in the same string S as the output.

Boundary Condition(s):
2 <= Length of S <= IOA4

Input Format:
The first line contains S.

Output Format:
The first line contains the number of occurrences of the last two characters of S in the same string S.

Example Input/Output 1:

Input:
hiabchi

Output:
2

Explanation:

The last two characters of the string hiabchi are h and i. Here the hi has occurred 2 times in the string hiabchi.
Hence the output is 2

Example Input/Output 2:

Input:
MOOONOO

Output:
3


Sollution: Done in Python

"""
s=input().strip()
a=s[-2:];b=0
for i in range(len(s)-1):
    if(s[i]==a[0] and s[i+1]==a[1]):
        b+=1
print(b)