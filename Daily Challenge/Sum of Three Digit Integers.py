"""

Sum of Three Digit Integers

The program must accept an integer N (where the number of digits in N is always divisible by 3) as the input. The program
must split the integer N into three-digit integers (every three consecutive digits). Then the program must print the sum S of
those three-digit integers as the output.

Boundary Condition(s):
100 <= N <= 999999999

Input Format:
The first line contains N.

Output Format:
The first line contains S.

Example Input/Output 1:

Input:
210045

Output:
255

Explanation:
Here N = 210045.
The first three-digit integer of 210045 is 210.
The last three-digit integer of 210045 is 045.

So their sum 255 (210 + 045) is printed as the output.


Example Input/Output 2:

Input:
100100

Output:
200


Max Execution Time Limit: 1000 millisecs


Solution: Done in Python

"""

s=input()
a=[i for i in range(len(s)+1) if(i%3==0)]
b=0
for i in range(len(a)-1):
    b+=int(s[a[i]:a[i+1]])
print(b)