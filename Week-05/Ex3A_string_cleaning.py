name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"


#Lab 2: using lower, upper, title

print(name_1.lower())
print(name_2.lower())
print(name_3.lower())
print()

#OUTPUT
#priya sharma
#bob nguyen
#latonya williams

print(name_1.title())
print(name_2.title())
print(name_3.title())
print()

#OUTPUT
#Priya Sharma
#Bob Nguyen
#Latonya Williams

print(salary_1.replace("$", ""))
print(salary_2.replace("$", ""))
print()

#OUTPUT 
#82,500
#74,000

salary_1_int = int(salary_1.replace("$", "").replace(",", ""))
print(salary_1_int)
print(type(salary_1_int))
print()

#OUTPUT
#82500
#<class 'int'>

salary_2_int = int(salary_2.replace("$", "").replace(",", ""))
print(salary_2_int)
print(type(salary_2_int))

#OUTPUT
#74000
#<class 'int'>