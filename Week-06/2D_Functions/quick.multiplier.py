
# Step 1: Create the doubler lambda
doubler = lambda n: n * 2

# Step 2: Test doubler with different values
print(doubler(8))
print(doubler(-4))
print(doubler('banana'))


# Step 3: Create the tripler lambda
tripler = lambda n: n * 3

# Step 4: Test tripler with the same values
print(tripler(8))
print(tripler(-4))
print(tripler('banana'))


# Step 5: Create a function that returns a multiplier lambda
def multiplier(x):
    return lambda n: n * x

# Create multiplier variables
quadrupler = multiplier(4)
quintupler = multiplier(5)
sextupler = multiplier(6)
septupler = multiplier(7)
octupler = multiplier(8)
nonupler = multiplier(9)
decupler = multiplier(10)

# Test a few examples
print(quadrupler(2))      # 2 * 4
print(quintupler('hi'))   # string repetition
print(decupler(3))        # 3 * 10
