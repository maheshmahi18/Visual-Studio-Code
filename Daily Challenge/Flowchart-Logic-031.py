"""

Flowchart Logic 031


Start
|
Input: x, y
|
Initialize val to 0
|
While x > 0 or y > 0:
|   |
|   If x > 0:
|   |   |
|   |   Append the last digit of x to val
|   |   Update x by removing the last digit
|   |
|   If y > 0:
|   |   |
|   |   Append the last digit of y to val
|   |   Update y by removing the last digit
|
Output: val
|
End

This code should work correctly for both input cases:

Input 1: 5122 3794
Output 1: 24291753

Input 2: 253 24907
Output 2: 37502942

Sollution: Done in Python

"""

val = 0
x, y = map(int, input().split())
while x > 0 or y > 0:
    if x > 0:
        val *= 10
        val += x % 10
        x //= 10
    if y > 0:
        val *= 10
        val += y % 10
        y //= 10
print(val)
