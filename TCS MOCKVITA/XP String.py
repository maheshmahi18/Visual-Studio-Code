"""
XP STRING

The program should accept integer N>
Next take n strings with given characters [A,B,C,D] form string
Let the letters has values for A:1 , B:2 , C:3 , D:4
Find the average of string and print maximum average string

Sample Input/Output

Input 1:
Enter no of strings required:
3
Enter 3 strings using these characters A, B, C, D:
AAA BBB CCC

Output 1:
String with the highest average position value: CCC

Input 2:
Enter no of strings required:
4
Enter 4 strings using these characters A, B, C, D:
AABB BBCC CCDD DDAA

Output 1:
String with the highest average position value: CCDD

"""

print("Enter no of strings required: ")
n = int(input())
print(f'Enter {n} strings using these characters A, B, C, D: ')
a = list(map(str, input().split()))
b = "ABCD"
c = []
for i in a:
    d = 0
    for j in i:
        d += (b.index(j) + 1)
    c.append(d / len(i))

max_avg_position = max(c)
max_avg_position_index = c.index(max_avg_position)

print("String with the highest average position value: ", a[max_avg_position_index])
