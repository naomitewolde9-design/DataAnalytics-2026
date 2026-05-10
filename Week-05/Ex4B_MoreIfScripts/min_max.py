a = 33
b = 31
c = 36

#finding the smallest 
if a < b and a < c:
    smallest = a
elif b < a and b < c:
    smallest = b
else:
    smallest = c 

#finding the largest 
if a > b and a > c:
    largeest = a 
elif b > a and b > c:
    largest = b 
else:
    largest = c 

print("The smallest out of a, b, and c is:", smallest)
print("The largest out of a, b, c is:", largest)

#The smallest out of a, b, and c is: 31
#The largest out of a, b, c is: 36