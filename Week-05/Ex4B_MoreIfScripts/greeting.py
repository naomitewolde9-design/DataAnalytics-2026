hour = 14 # I put in multiple different hours for different outputs

if 5 <= hour < 10:
    print("Good Morning")
#using military time so this would be from 5am to 10am
elif 10 <= hour < 17: 
    print("Good day!")
#10am to 5pm
elif 17 <= hour < 23: 
    print("Good evening")
#5pm to 11pm
elif hour >= 23 or hour < 5: 
    print("What are you doing up so late??")
#11pm to 5am

# Good day!