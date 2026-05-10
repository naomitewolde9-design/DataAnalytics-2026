dept = { 1: 'Marketing', 5: "Human Resources", 
        10: "Accounting", 12: "Legal", 18: "IT",
          20: "Customer Relations"}

dept_lookup = int(input('Type in your depatment code: '))

if dept_lookup == 1:
    print(f"Your department is {dept[1]}")
elif dept_lookup == 5:
    print(f"Your department is {dept[5]}")
elif dept_lookup == 10:
    print(f"Your department is {dept[10]}")
elif dept_lookup == 12:
    print(f"Your department is {dept[12]}")
elif dept_lookup == 18:
    print(f"Your department is {dept[18]}")
elif dept_lookup == 20:
    print(f"Your department is {dept[20]}")
else:
    print("Your department is not found.")