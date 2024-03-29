"""

Digits in Ascending Order

The program must accept an integer N as the input. The program must print YES if all the digits in N are in ascending order.
Else the program must print NO as the output.

Boundary Condition(s):
10 <= N <= 10^7

Input Format:
The first line contains N.

Output Format
The first line contains either YES or NO.

Example Input/Output 1:

Input:
2579

Output:
YES

Explanation:
In 2579 all the digits are in ascending order.

So YES is printed as the output


Example Input/Output 2:

Input:
52738

Output:
NO


Max Execution Time Limit: 500 millisecs

"""

s=input()
a=[i for i in range(len(s)-1) if(s[i+1]>s[i])]
if(len(a)+1==len(s)): print("YES")
else: print("NO")