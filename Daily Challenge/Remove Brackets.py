"""

Remove Brackets

The program must accept a string S as the input. Some characters in the string S surrounded by anyone of the brackets (),[]
and {}. The program must remove those brackets from the string S and print it as the output

Boundary Condition(s):
1 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format
The first line contains the modified string S.

Example Input/Output 1:

Input:
Jac[k]po(t)

Output
Jackpot

Explanation:
Here the string S is Jaclklpo(t)
After removing the brackets [] and (), the string becomes Jackpot.
So Jackpot is printed as the output.


Example Input/Output 2:

Input:
D(v)[o]{r}a[k]

Output:
Dvorak


Max Execution Time Limit: 1000 millisecs

Solution: Done in Python

"""

s=input()
a=[i for i in s if i.isalpha()]
print("".join(a))