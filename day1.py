# Advent of Code 2024
# Day 1: Historian Hysteria
# Part 1

list1 = []
list2 = []
distList = []
count = 0

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
    parts = line.split()
    list1.append([int(parts[0])])
    list2.append([int(parts[1])])
    count += 1
# Sort lists from smallest to largest
list1.sort()
list2.sort()
# TODO: Find distance between each list input (larger - smaller = distance)
for i in count:
    dist = distCalc(list1[i], list2[i])
    ## TODO: Put distances into new list
    distList.append(dist)

## TODO: Find and print Sum of distances list
sum = sum(distList)
print(f"The total distance between lists is ", sum)


# Part 2
