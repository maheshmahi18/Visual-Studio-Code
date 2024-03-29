"""

The program must accept an integer N as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Note: All the digits in N are non-zero digits.

Boundary Condition(s):
11 <= N <= 10^4

Input Format:
The first line contains N.

Output Format:
The lines contain the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:
Input:
651

Output:
51 51 51 51 51 51
61 61 61 61 61
65


Example Input/Output 2:

Input:
9845

Output:
845 845 845 845 845 845 845 845 845
945 945 945 945 945 945 945 945
985 985 985 985
984 984 984 984 984

Max Execution Time Limit: 1000 millisecs


Solution: Done in Python

"""

s=input().strip()
for i in  range(len(s)):
    a=int(s[i])
    b=[s[j] for j in range(len(s)) if i!=j and s[j]!='0']
    res="".join(b)
    if a!=0:
        print((res+' ')*a)