#Example 6

U = set([0,1,2,3,4,5,6,7,8,9,10])
A = set([3,6,9])
B = set([2,4,6,8])


# Example of intersection operation
AB=A & B
print ('Intersection of A and B = %r \n') %AB

# Example of finding the complement of B

Bc=U - B
print ('B complement = %r \n') %Bc

Bans = A & Bc
print (Bans)



