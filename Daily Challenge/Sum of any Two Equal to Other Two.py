"""

Sum of any Two Equal to Other Two

The program must accept four integers as the input. The program must print YES if the sum of any two integers is equal to the sum of the remaining integers. Else the program must print NO as the output.

Boundary Condition(s):
1 <= Each integer value <= 10^7

Input Format:
The first line contains four integers separated by a space.

Output Format:
The first line contains YES or NO.

Example Input/Output 1:

Input:
2 3 1 4

Output:
YES

Explanation:

The sum of 2 and 3 is 5.
The sum of 1 and 4 is 5.
Here, both results are the same.

Hence the output is YES

Example Input/Output 2:

Input:
3 5 8 2

Output:
NO


Solution: Done in Python


"""

a=list(map(int,input().split()))
b=[]
for i in range(len(a)):
    b.append([a[i]+a[j] for j in range(len(a)) if i!=j])
c=set(b[0]).intersection(b[1],b[2],b[3])
if len(c)>=1: print("YES")
else: print("NO")