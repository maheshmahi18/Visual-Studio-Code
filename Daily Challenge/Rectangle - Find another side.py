"""

Rectangle - Find another side

The length of one side S (in cm) of a rectangle and its perimeter P (in cm) are passed as the input. The program must print the
length of another side of the rectangle with the precision up to two decimal places as the output.

Formula: Perimeter of a rectangle = 2 x (length + breadth)

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 10^6

Input Format:
The first line contains S and P separated by a space.

Output Format:
The first line contains the length of another side of the rectangle.

Example Input/Output 1:

Input:
4 18

Output:
5.00


Example Input/Output 2:

Input:
3 15

Output:
4.50


Max Execution Time Limit: 1000 millisecs


Solution: Done in Python

"""

a,b=map(int,input().split())
print("%.2f"%((b/2)-a))