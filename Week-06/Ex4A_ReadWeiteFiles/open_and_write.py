
import os

print(os.getcwd()) # location of file finder

f = open("about_me.txt", "a")

f.write("Name:Naomi Tewolde\n")
f.write("Place of birth: Charlotte, NC\n")
f.write("Pets growing up: A cat named Miko\n")
f.write("Travel for one week: Japan\n")
f.write("Live for one year: Italy\n")

f.write("\nPerfect night out: I would go to a nice restaurant, then watch a movie, and end the night with a walk on the beach.\n")

# Closes the file
f.close()


#reads file in terminal
f = open("about_me.txt", "r")

# Read and print the entire file
print(f.read())

# Close the file
f.close()




f = open("about_me.txt", "r")

# print(f.read())
# print(f.read(50))

# a) readline experiments
print(f.readline(10))   # reads first 10 characters of the first line
print(f.readline())     # reads the rest of that line

# b) for loop to read next lines
for i in range(1, 5):
    print(f.readline())

f.close()




f = open("about_me.txt", "r")

# a) readlines experiments
print(f.readlines(1))  

# b) second readlines(1) and (-1)
print(f.readlines(-1))

# c) readlines(10) and try (100)
print(f.readlines(100))

f.close()




f = open("about_me.txt", "r")

# a) First 50 characters
first_part = f.read(50)

# b) Next four lines using readline() and a list
next_lines = []

for i in range(4):
    next_lines.append(f.readline())

# c) Next 100 characters using readlines()
last_part = f.readlines(100)

# Close file
f.close()

# Step 3: Print formatted output
print("First 50 characters:", first_part)
print("\nNext four lines, as list by line:", next_lines)
print("\nNext 100 characters, as list by line, rounded up to complete lines:", last_part)

