#Example 7

U = set([0,1,2,3,4,5,6,7,8,9,10,11,12])
A = set([1,3,5,7,9,11])
B = set([3,6,9,12])
C = set([1,2,3,4,5])

print("A union B")
AuB = A | B
print(AuB)

nC = U-C
print("(A U B) U C'")

ans = ((A | B) & nC)
print(ans)