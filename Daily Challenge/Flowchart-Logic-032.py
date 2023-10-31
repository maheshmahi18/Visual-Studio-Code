"""

Flowchart Logic - 032

Start
|
|  [User Input] Enter a value for 'n'
|       |
|       v
|    +-----> [Assign n to temp]
|    |      |
|    |      v
|    |    +----> [Initialize sum = 0]
|    |    |
|    |    v
|    |  +-----> [Loop while temp is not 0]
|    |  |      |
|    |  |      v
|    |  |    +-----> [Get last digit of temp]
|    |  |    |
|    |  |    v
|    |  |  +-----> [Add last digit to sum]
|    |  |  |
|    |  |  v
|    |  | |-------> [Remove last digit from temp]
|    |  |  |
|    |  |  v
|    |  |  |-------> [End of Loop]
|    |  |  |
|    |  |  v
|    |  | |-------> [Check if n is divisible by sum]
|    |  |  |
|    |  |  v
|    |  | |-------> [Print "YES" or "NO"]
|    |  |
|    |  v
|    | |-------> [Print sum]
|    |
|    v
| |-------> [End]

Explanation:

Certainly! Here's a concise text-based flowchart explanation for the updated Python code:

1. User inputs a value 'n'.
2. Initialize 'temp' to the same value as 'n'.
3. Initialize 'sum' to 0.
4. Check if 'temp' is not equal to 0.
   a. If 'temp' is not 0, proceed to the next steps.
   b. If 'temp' is 0, skip to step 8.
5. Get the last digit of 'temp'.
6. Add the last digit to 'sum'.
7. Remove the last digit from 'temp'.
8. Check if 'n' is divisible by 'sum'.
   a. If 'n' is divisible by 'sum', print "YES".
   b. If 'n' is not divisible by 'sum', print "NO".
9. Print the value of 'sum'.

This flowchart explains the logic of the updated Python code for checking if 'n' is divisible by the sum of its digits and printing "YES" or "NO" accordingly, and also prints the sum of the digits.

Sample Test Case 1:

Input:
9

Output: 
YES


Sample Test Case 2:

Input:
1234

Output: 
NO

Sollution: Done in Python


"""

n=int(input())
temp=n
sum=0
while(temp!=0):
    sum+=temp%10
    temp//=10
if(n%sum==0): print("YES")
else: print("NO")