"""

Substring from End

The program must accept a string S as the input. The program must print the substring values of S in reverse order as the output.

Boundary Condition(s):
2 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format:
The first line contains the substring values of S in reverse order.

Example Input/Output 1:

Input:
Brick

Output:
kckickrickBrick

Explanation:
In the string "Brick", the last one character is k. So k is printed.
The last two characters are c and k. So ck is printed.
The last three characters are i c and k. So ick is printed.
The last four characters are r i c and k. So rick is printed.
The last five characters are B r i c and k. So Brick is printed.

Example Input/Output 2:

Input:
dolphin

Output:
ninhinphinlphinolphindolphin

Max Execution Time Limit: 1000 millisecs


Solution: Done in Python

"""

s=input()
a=[s[i:] for i in range(len(s))]
b=sorted(a,key=len)
print("".join(b))