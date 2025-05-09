"""
C(n,k) = n! / (k! * (n-k)!)

import math
print("5!",  math.factorial(5) )
Enter n: 1
Output:
1

Enter n: 2
Output:
1 1

Enter n: 3
Output:
1 2 1

Enter n: 4
Output:
1 3 3 1

"""

import math

n = int(input("Enter n: "))

out_put = ""

for i in range(n + 1):
    for j in range(i):
        out_put += f"{math.comb(i - 1, j)} "
    out_put += "\n"
    # or the code below ;
    # out_put +=f"{math.factorial(m)//(math.factorial(i)*math.factorial(m-i))} "
print(out_put)
