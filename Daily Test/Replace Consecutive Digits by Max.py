"""

Replace Consecutive Digits by Max

The program must accept a string S containing alphabets and digits as the input. For each substring X containing only digits in
the string S, the program must replace the substring X by the largest digit in it Then the program must print the modified
string S as the output

Boundary Condition(s):
2 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format
The first line contains the modified string S.

Example Input/Output 1:

Input
abc132sdfg789090okokok30k

Output
abc3sdfg90kokok30k

Explanation:
In the given string abc132sdfg789090kokok30k
The first substring 132 is replaced by the largest digit 3.
The second substring 78909 is replaced by the largest digit 9.
The third substring 3 has only one digit so keep as it is.

So abc3sdfg90kokok30k is printed as the output.


Example Input/Output 2:

Input:
123562A

Output:
6A


Max Execution Time Limit: 500 millisecs

Solution: Done in Python

"""

s=input()
a="";b=[]
for i in s:
  if i.isalpha():
    if(len(b)>1):
      a+=str(max(b));b=[]
    a+=i
  else:
    b.append(int(i))
if(len(b)>0): a+=str(max(b));print(a)
else: print(a)