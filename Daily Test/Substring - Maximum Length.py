"""

Substring - Maximum Length

The program must accept two string values Sl and S2 are of equal length as the input. The program must print the common
substring which is having the maximum length and occurring at the same position in both string values. If there is more than
one such substring then print the first occurring one as the output.

Note: At least one character is always present at the same position in both string values.

Boundary Condition(s):
1 <= Length of Sl, S2 <= 1000

Input Format:
The first line contains Sl.
The second line contains S2.

Output Format:
The first line contains the common substring which is having the maximum length and occurring at the same position in both
string values.

Example Input/Output 1:

Input:
skillrack
SkillRack

Output:
kill

Explanation:

There are two substrings kill and ack occurring at the same position in both string values.
SK
Here the substring kill is having the maximum length. So kill is printed as the output.

Example Input/Output 2:

Input:
abcxxyzmn
abdxyzkmn

Output:
ab


Sollution: Done in Python

"""

a=input().strip()
b=input().strip()
c=[];d="";e=[]
for i in range(len(a)):
    if(a[i]!=b[i]):
        if(len(d)>=1):
            c.append(d)
            e.append(len(d))
            d=""
    else: d+=a[i]
c.append(d);e.append(len(d))
print(c[e.index(max(e))])