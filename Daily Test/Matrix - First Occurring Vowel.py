"""

Matrix - First Occurring Vowel

The program must accept a character matrix of size RxC as the input. The program must print the first occurring vowels from the top in each column of the matrix as the output.

Note: At least one vowel is always occurred in each column of the matrix.

Boundary Condition(s):
2 <= R, C <= 100

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C characters separated by a space.

Output Format:
The first line contains the first occurring vowels from the top in each column of the matrix.

Example Input/Output 1:

Input:
4 4
H N L A
y S I 0
h a O #
e F @ a

Output:
eaIA

Explanation:
The first occurring vowels from the top in each column of the matrix are highlighted below.

So ealA is printed as the output.


Example Input/Output 2:

Input:
3 7
o f w $ w E d
t v M i O i 1
2 E e @ R O u

Output:
oEeiOEu


Max Execution Time Limit: 500 millisecs


Solution: Done in Python

"""

a,b=map(int,input().split())
c=[];d=""
for i in range(a):
    c.append(list(map(str,input().split())))
for i in range(b):
    for j in range(a):
        if c[j][i] in "aeiouAEIOU": d+=c[j][i];break
print(d)