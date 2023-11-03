"""

Decrypt the Code

The program must accept a string S(encrypted string) containing only .(Dots) and -(Hyphens) as the input. The encryption
algorithm is given below.

- Digit 0 is encrypted as . (Single Dot).
- Digit 1 is encrypted as -. (Hyphen and Dot).
- Digit 2 is encrypted as -- (Hyphens).

The program must decrypt the string S and print it as the output.

Note: The String S is always a valid encrypted string.

Boundary Conditions:
1 <= Length of S <= 1000

Input Format:
The first line contain S.

Output Format:
The first line contains the decrypted string of S.

Example Input/Output 1:

Input:
.-.--

Output:
012

Explanation:
012 can be decrypted as ".-.--", So 012 is printed as the output.

Example Input/Output 2:

Input:
--.

Output:
20


Sollution: Done in Python

"""
s=input().strip()
a=[]
for i in range(len(s)-1):
  if(i not in a):
    if(s[i]+s[i+1]=='--'): print(2,end=""); a.append(i); a.append(i+1)
    elif(s[i]+s[i+1]=='-.'): print(1,end=""); a.append(i); a.append(i+1)
    elif(s[i]=='.'): print(0,end=""); a.append(i)
  else: continue
if(len(s)-1 not in a):
  if(s[len(s)-1]=='.'): print(0,end="")
  