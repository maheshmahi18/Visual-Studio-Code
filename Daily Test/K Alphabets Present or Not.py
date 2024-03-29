"""

K Alphabets Present or Not


The program must accept a string S and an integer K as the input. The program must print YES if the first K lower case alphabets are present atleast once in the string S. Else the program must print NO as the output.

Boundary Condition(s):
1 <= Length of S <= 100
1 <= K <= 26

Input Format:
The first line contains S.
The second line contains K.

Output Format:
The first line contains either YES or NO.

Example Input/Output 1:

Input:
afehijklmnopzqrcstuvdwxgyb
5

Output:
YES

Explanation:
Here K = 5.
The first 5 lower case alphabets are a b c d e, which are present in the string afehijklmnopzqrcstuvdwxgyb.
So YES is printed.


Example Input/Output 2:

Input:
BdbAarCst
3

Output:
NO


Max Execution Time Limit 500 millisecs


Solution: Done in Python


"""

s=input().strip()
k=int(input())
a="abcdefghijklmnopqrstuvwxyz"
b=[i for i in range(k) if a[i] in s]
if(len(b)==k): print("YES")
else: print("NO")