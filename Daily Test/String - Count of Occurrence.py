"""

String - Count of Occurrence

The program must accept a string S containing only alphabets as the input. The program must print the alphabets of S
based on the count of their occurrence. If more than one alphabets have the same occurrence count, the program must print
the alphabets in the alphabetical order as the output.

Note: The string S is case sensitive.

Boundary Condition(s):
1 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format:
The first line contains the alphabets of S based on the
count of their occurrence.

Example Input/Output 1:

Input:
AAAbbbbccccccdddEEE

Output:
cbAEd

Explanation:
The count of occurrence of c is 6, so c is printed at first.
The count of occurrence of b is 4, so b is printed at
second.
The alphabets A, d and E have the same count of
occurrence 3, so they are printed in alphabetical order.

Hence the output is cbAEd


Example Input/Output 2:

Input:
SkillRack

Output:
klRSaci


Max Execution Time Limit: 500 millisecs


Solution: Done in Python

"""

s=input()
a={}
for i in s:
    a[i]=a.get(i,0)+1
b=sorted(a.items(), key=lambda x: (-x[1],x[0]))
print("".join([i[0] for i in b]))