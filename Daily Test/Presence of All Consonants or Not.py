"""

Presence of All Consonants or Not

The program must accept a string S containing only lower case alphabets as the input The program must print YES if all the consonants are present in the string S (in any order). Else the program must print NO as the output

Boundary Condition(s):
26 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format:
The first line contains either YES or NO.

Example Input/Output 1:

Input
abcdefghijklmnopqrstuvwxyz

Output:
YES

Explanation:
All the 21 consonants (bcdfghjklmnpqrstvwxyz) are present in the string abcdefghijklmnopqrstuvwxyz.

So YES is printed,

Example Input/Output 2:

Input
pqbchjrgstvklmndfhjbcgstmns

Output:
NO


Solution: Done in Python

"""

s=input()
a="bcdfghjklmnpqrstvwxyz"
b=[i for i in s]
b=set(b)
c=0
d=[c for i in b if i in a]
if(len(d)==len(a)): print("YES")
else: print("NO")