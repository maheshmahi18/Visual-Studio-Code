"""

Flowchart-Logic-034

   [Start]
     |
     v
   [Initialize 'sum' to 0]
     |
     v
   [Read 'x' from input]
     |
     v
   [While x > 0]
     |
     v
   [Calculate x % 1000 and add to 'sum']
     |
     v
   [Update 'x' by 'x // 1000']
     |
     v
   [End of Loop]
     |
     v
   [Print 'sum']
     |
     v
   [End]
     |
     v
   [Exit]


Sample Input/Ouput:

Input 1:
1234567
   
Output 1:
802

Explanation:

The code first reads the integer 1234567.
It enters the loop and iteratively calculates x % 1000, which is 567, and adds it to the sum.
Then, it updates x by performing integer division x // 1000, which results in 1234.
The loop continues, and x % 1000 is calculated again, which is 234, and added to the sum.
Finally, x is updated to 1, and the loop continues until x becomes 0.
The code prints the final value of sum, which is 802


Input 2:
9876543210

Output 2:
1638

Sollution: Done in Python


"""

sum=0
x=int(input())
while(x>0):
    sum+=x%1000
    x//=1000
print(sum)