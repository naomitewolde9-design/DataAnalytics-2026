#ValueError
try:
    x = int("hello")   # cannot convert text to integer
except ValueError:
    print("ValueError: You tried to convert a string into an integer")
else:
    print(x)
finally:
    print("Let's try another one...\n")
