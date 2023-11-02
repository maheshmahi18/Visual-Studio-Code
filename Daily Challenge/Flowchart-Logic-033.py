"""

Flowchart Logic - 033

Start
|
Input 'n' (an integer)
|
Calculate 'unit' by finding n % 10
|
While 'n' is less than 9:
|   |
|   Divide 'n' by 10 (integer division)
|   |
|   Calculate 'val' by multiplying 'n' by 10 and adding 'unit'
|   |
|   Square 'val'
|
Output the result of 'val' squared
|
End

Explanation:

The input is 98.
The unit is calculated as 98 % 10, which is 8.
The while loop condition is met because 98 is less than 9.
'n' is divided by 10, and it becomes 9.
'val' is calculated as 9 * 10 + 8, which is 98.
The square of 'val' is 98 * 98, which is 9604.

Sample Input/Output

Input 1:
5

Output 1:
3025

Input 2:
98

Output 2:
9604

Sollution: Done in Python

"""
n=int(input())
unit=n%10
while(n>9):
    n//=10
val=n*10
val+=unit
print(val*val)