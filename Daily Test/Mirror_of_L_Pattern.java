/*

Mirror of L Pattern

The program must accept a string S as the input. The program must print the desired pattern as shown in the Example Input/Output section.

Boundary Condition(s):
3 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format:
The lines containing the desired pattern as shown in the Example Input/Output section.

Example Input/Output 1:

Input:
skillrack

Output:
skillrack
kkillrack
iiillrack
lllllrack
lllllrack
rrrrrrack
aaaaaaack
cccccccck
kkkkkkkkk


Example Input/Output 2:

Input:
huge

Output:
huge
uuge
ggge
eeee


Max Execution Time Limit: 500 millisecs


Solution: Done in Java

*/

import java.util.*;

public class Mirror_of_L_Pattern {
    public static void main(String[] args) {
      Scanner sc=new Scanner(System.in);
      String s=sc.nextLine();
      for(int i=0; i<s.length(); i++){
        for(int k=0; k<i; k++){
          System.out.print(s.charAt(i));
        }
        for(int j=i; j<s.length(); j++){
          System.out.print(s.charAt(j)+"");
        }
        System.out.println();
      }
  }
}