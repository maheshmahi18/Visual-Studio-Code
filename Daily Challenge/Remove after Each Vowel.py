"""

Remove after Each Vowel

The program must accept a string S as the input. For each vowel CH in the string S (from left to right), the program must
remove the next character of CH from the string S. Then the program must print the modified string as the output.

Boundary Condition(s):
1 <= Length of S <= 1000

Input Format:
The first line contains S.
Output Format:

The first line contains the modified string S.

Example Input/Output 1:

Input:
skillrack

Output:
skilrak

Explanation:
Here the string is skillrack
The first vowel in skillrack is i. The next character of i is I, so I is removed from the string skillrack. Now the string becomes
skilrack.
The second vowel in skillrack is a. The next character of a is c, so c is removed from the string skilrack. Now the string becomes
skilrak.

Finally, the modified string skilrak is printed as the output.


Example Input/Output 2:

Input:
Aerospace

Output:
Aropae


Example Input/Output 3:

Input:
AeI#oU123

Output:
AIo123


Max Execution Time Limit: 500 millisecs

Solution: Done in Python


"""


def check(a):
  b="aeiouAEIOU"
  c=[i for i in a]
  d=""
  while(len(c)>1):
    if c[0] in b:
      d+=c[0]
      c.remove(c[1]);c.remove(c[0])
    else:
      d+=c[0]
      c.remove(c[0])
  if(len(c)==1): d+=c[0]
  print(d)

s=input().strip()
check(s)