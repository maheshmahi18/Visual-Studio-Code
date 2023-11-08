"""

Same Case - Vowels

The program must accept a string S containing only alphabets as the input. The program must print YES if all the vowels in the string S are same case (i.e either upper case or lower case). Else the program must print NO as the output.

Note: At least one vowel is always present in the string S.

Boundary Condition(s):
1 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format
The first line contains YES or NO.

Example Input/Output 1:

Input:
SkillRack

Output:
YES

Example Input/Output 2:

Input:
Information

Output:
NO

Explanation:

The string Sk IIR ck contains two vowels i and a.
Here i and a are in lower case. So YES is printed as the output.

Example Input/Output 3:

Input:
ElgHtEEn

Output:
YES


Solution: Done in Python

"""
s=input()
a="aeiou";b="AEIOU"
c=[i for i in s if i in a]
d=[i for i in s if i in b]
if(len(c)==0 or len(d)==0): print("YES")
else: print("NO")