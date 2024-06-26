# Using a list comprehension, write a program that receives numbers, separated by comma and space ", ", and prints
# all the positive, negative, even, and odd numbers on separate lines as shown below.
# Note: Zero is counted as a positive number
#
# nums = [int(num) for num in input().split(', ')]
#
# positive_nums = [n for n in nums if n >= 0]
# negative_nums = [n for n in nums if n < 0]
# even_nums = [n for n in nums if n % 2 == 0]
# odd_nums = [n for n in nums if not n % 2 == 0]
#
# print(f'Positive: {", ".join([str(n) for n in positive_nums])}')
# print(f'Negative: {", ".join([str(n) for n in negative_nums])}')
# print(f'Even: {", ".join([str(n) for n in even_nums])}')
# print(f'Odd: {", ".join([str(n) for n in odd_nums])}')

nums = [int(n) for n in input().split(", ")]

neg_n = []
pos_n = []
odd = []
even = []

[even.append(num) if num % 2 == 0 else odd.append(num) for num in nums]
[pos_n.append(num) if num >= 0 else neg_n.append(num) for num in nums]

print("Positive:", end=" ")
print(*pos_n, sep=", ")
print("Negative:", end=" ")
print(*neg_n, sep=", ")
print("Even:", end=" ")
print(*even, sep=", ")
print("Odd:", end=" ")
print(*odd, sep=", ")