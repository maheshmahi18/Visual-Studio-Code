"""

Square Brackets - String

The program must accept a string S with spaces as the input. The program must convert all the alphabets between each pair of
square brackets [ ] to upper case alphabets. Finally, the program must print the modified string S as the output.

Boundary Condition(s):
3 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format:
The first line contains the modified string S.

Example Input/Output 1:

Input:
uhuu [ntu e]tuhnt[uheo

Output:
uhuu [NTU E]tuhnt[uheo

Explanation:

In the string uhuu [ntu e]tuhnt[uheo, the alphabets within the pair of square brackets are n t u e.
After coverting those alphabets into uppercase the string becomes uhuu [NTU E]tuhnt[uheo.

Hence the output is uhuu [NTU E]tuhnt[uheo


Example Input/Output 2:

Input:
[robert [was] a good [king]

Output:
[robert [WAS] a good [KING]


Example Input/Output 3:

Input:
[as[df]er]

Output:
[as[DF]er]


Max Execution Time Limit: 500 millisecs


Solution: Done in Python


"""

def cap(s):
  a=[i.upper() for i in s]
  b="".join(a)
  return b

s=input().strip()
a="";b=[];e=len(s)-1
for i in range(len(s)-1):
  if s[i]=='[':
    c="["
    for j in range(i+1,len(s)):
      if(s[j]=='['):
        a+=c;b.append(j)
        break
      elif(s[j]==']'):
        a+=cap(c)+']';b.append(j)
        break
      else:
        if(j==e):
          a+=c+s[len(s)-1]
          break
        c+=s[j];b.append(j)
  else:
    if(i not in b):
      a+=s[i]
if(len(s)-1 not in b):
  a+=s[len(s)-1]
print(a)