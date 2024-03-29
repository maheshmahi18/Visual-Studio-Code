"""

String Triangle Pattern

The program must accept a string S as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
3 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format:
The lines containing the desired pattern as shown in the Example Input/Output section.


Example Input/Output 1:

Input:
skillrack

Output:
s********
ks*******
ski******
liks*****
skill****
rlliks***
skillra**
carlliks*
skillrack


Example Input/Output 2:

Input:
hope

Output:
h***
oh**
hop*
epoh


Max Execution Time Limit: 500 millisecs


Solution: Done in Python


"""

s=input()
c=1
for i in range(1,len(s)+1):
    a=s[:i]
    if(c%2!=0):
        print(a,end="");c+=1
        b=['*' for j in range(i,len(s))]
        print("".join(b))
    else:
        print(a[::-1],end="");c+=1
        b=['*' for i in range(i,len(s))]
        print("".join(b))