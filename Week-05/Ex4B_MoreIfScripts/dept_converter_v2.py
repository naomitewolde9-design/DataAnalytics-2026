dept = { 1: 'Marketing', 5: "Human Resources", 
        10: "Accounting", 12: "Legal", 18: "IT",
          20: "Customer Relations"}

dept_lookup = int(input('Type in your depatment code: '))

match dept_lookup:

    case 1:
         print(f"Your department is {dept[1]}")
    
    case 5:
          print(f"Your department is {dept[5]}")

    case 10:
          print(f"Your department is {dept[10]}")
    
    case 12:
           print(f"Your department is {dept[12]}")

    case 18:
           print(f"Your department is {dept[18]}")

    case 20:
          print(f"Your department is {dept[20]}")

    case _:
          print("Your department is not found")
            
        
          
