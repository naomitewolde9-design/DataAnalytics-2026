import random
import math
import statistics

# create variables
vals_1_100 = range(1, 100) # nums from 1-99, python stops before 100
vals_sample = random.sample(vals_1_100, 75) # picking 75 nums at random with no repeats 
vals_choices = random.choices(vals_1_100, k=200) # picks 200 nums with repeats ALLOWED 
radius = random.randint(3, 10) # random int between 3-10 
pi = math.pi # stores value of pi 


#QUESTION 3

# PART 1:
# creating variables
vals_1_100 = range(1, 101)  # 1–100 (include 100)
vals_sample = random.sample(vals_1_100, 75)


# calculating the sum of the 75 sampled values
sample_sum = sum(vals_sample)

# calculating the average (mean)
sample_avg = statistics.mean(vals_sample)


# calculating the median
sample_median = statistics.median(vals_sample)

#OUTPUT:
#Experimenting with a subset of integers 1-100:
#Sum of 75 sample values from 1 to 100: 3507
#Average of 75 sample values: 46.76
#Median of 75 sample values: 46


# PART 2: 

# calculating the average (mean)
choices_avg = statistics.mean(vals_choices)

# calculating the median
choices_median = statistics.median(vals_choices)

# calculating the mode (most frequent value)
choices_mode = statistics.mode(vals_choices)

# calculating the standard deviation
choices_std = statistics.stdev(vals_choices)

# calculating the variance
choices_var = statistics.variance(vals_choices)

#OUTPUT:
#Experimenting with a superset of 200 values, integers 1-100:
#Average of 200 values: 52.935
#Median of 200 values: 53.0
#Mode of 200 values: 90
#Standard deviation of 200 values: 29.449569789795234
#Variance of 200 values: 867.2771608040201


# PART 3:

# a random radius 
radius = random.uniform(1, 10)

# Calculating the area
area = math.pi * radius ** 2

# Rounding up and down
area_up = math.ceil(area)
area_down = math.floor(area)


print()
print("_Experimenting with a subset of integers 1-100:\n")
print("Sum of 75 sample values from 1 to 100:", sample_sum)
print("Average of 75 sample values:", sample_avg)
print("Median of 75 sample values:", sample_median)
print()


print("_Experimenting with a superset of 200 values, integers 1-100:\n")
print("Average of 200 values:", choices_avg)
print("Median of 200 values:", choices_median)
print("Mode of 200 values:", choices_mode)
print("Standard deviation of 200 values:", choices_std)
print("Variance of 200 values:", choices_var)
print()


print("_Modeling a random circle:\n")
print(f"Radius = {radius:.2f}, area = {area_up} (rounded up to the nearest int)")
print(f"Radius = {radius:.2f}, area = {area_down} (rounded down to the nearest int)")