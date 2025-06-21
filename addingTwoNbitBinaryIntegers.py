import random

n = random.randint(1,10)
# a = b = n
c = n+1
A = random.choices(range(0,2),k=n)
B = random.choices(range(0,2),k=n)
print(A)
print(B)
C = [0]*c
# print(C)

add = 0
carry = 0
for iterator in range(n):
    add = A[iterator]+B[iterator]+carry
    carry = add//2
    add = add%2
    C[iterator] = add
C[n] = carry
print(C)