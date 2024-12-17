# Advent of Code 2024
# Day 1: Historian Hysteria
# Part 1

list1 = []
list2 = []
distancelist = []
dis = 0

# Read file
file = open("data/day1.txt", "r")

# Function to find distance between 2 numbers
def disCalc(num1, num2):
    if(num1 > num2):
        distance = num1 - num2
    else:
        distance = num2 - num1
    return distance

# Put Data into 2 Lists (list1 and list2)
for line in file:
    list1.append(int(line.split()[0].strip()))
    list2.append(int(line.split()[1].strip()))
# Sort lists from smallest to largest
list1.sort()
list2.sort()
# Find distance between each list input (larger - smaller = distance)
for i in range(0, len(list1)):
    dis += abs(list2[i] - list1[i])

# Print Sum of distances list

print(f"The sum of the distances is ", dis)

# Part 2
