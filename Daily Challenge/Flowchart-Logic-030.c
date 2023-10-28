/*

Flowchart Logic 030

Please fill in the lines of code to implement the logic present in the flowchart.

		
				Start
				  |
Declare four integers variables N,X,Y and maxSum
				  |
			Assign 0 to maxSum
				  |
			Read the value of N
				  |
Declare an integer variable ctr and assign 1 to it
				  |
		{ Check if ctr <= N/2 } -->[If NO] --> Print the value of maxSum --> End
				  |	  
			  [If YES]
				  |
	  Read the values of X and Y
				  |
       { check if X+Y > maxSum } -->[If NO] --> Increment the value of ctr by 1
				  |
			  [If YES]
				  |
		Assign X+Y to maxSum
				  |
  	Increment the value of ctr by 1

Sample Input/Output

Test Case 1:

Input:
	N = 6
	X = 2 5 3 1 8 4
	Y = 3 7 2 4 5 6

Output:
	12


Test Case 2:

Input:
	N = 3
	X = 1 3 5
	Y = 2 4 6

Output:
	4



Sollution: Done in C

*/


#include <stdio.h>
#include <stdlib.h>

int main()
{
	int N,X,Y,maxSum;
  	maxSum=0;
  	scanf("%d",&N);
  	for(int ctr=1;ctr<=N/2;ctr++)
	{
		scanf("%d %d",&X,&Y);
		if(X+Y>maxSum)
		{
			maxSum=X+Y;
    	}
  	}
 	printf("%d",maxSum);
}