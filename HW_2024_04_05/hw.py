# with open('HW_2024_04_05/text.txt', 'r') as file:
#     line = file.read()
# print(line[::-1])


# with open('HW_2024_04_05/data.txt', 'r') as file:
#     lines = file.readlines()

# for line in reversed(lines):
#     print(line.strip()) 

# import re

# def str_to_int(s):
#     return int(s)

# with open('HW_2024_04_05/nums.txt', 'r') as file:
#     text = file.read()

# numbers = re.findall(r'-?\d+', text)

# total_sum = sum(map(str_to_int, numbers))

# print(total_sum)


# import random


# random_numbers = [random.randint(111, 777) for _ in range(25)]

# with open('HW_2024_04_05/random.txt', 'w') as file:
#     for num in random_numbers:
#         file.write(str(random.randint(111, 777)) + '\n')

# lines = 0
# file = open("HW_2024_04_05/input.txt")
# for line in file:
#     lines +=1
#     print (lines, line)