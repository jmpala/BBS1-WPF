"""
This program will give a random number to convert it into another
"""
import random

decimal_prefixes = ["K", "M", "G", "T"]
decimal_values = [10**3, 10**6, 10**9, 10**12, 10**15, 10**18, 10**21, 10**24]

binary_prefixes = ["Ki", "Mi", "Gi", "Ti"]
binary_values = [2**10, 2**20, 2**30, 2**40, 2**50, 2**60, 2**70, 2**80]

bit_byte = ["b", "B"]

start = 1
end = 1024


def generate_number():
    number = random.randint(start, end)
    prefix_index = random.randint(0, len(decimal_prefixes) - 1)
    b_B = bit_byte[random.randint(0, len(bit_byte) - 1)]
    number_str = ""
    prefix_value = 0
    if b_B == "b":
        number_str = str(number) + binary_prefixes[prefix_index] + b_B
        prefix_value = binary_values[prefix_index]
    else:
        number_str = str(number) + decimal_prefixes[prefix_index] + b_B
        prefix_value = decimal_values[prefix_index]
    return [number_str, prefix_value]


def generate_random_prefix():
    prefix_index = random.randint(0, len(decimal_prefixes) - 1)
    b_B = bit_byte[random.randint(0, len(bit_byte) - 1)]
    number_prefix = ""
    prefix_value = 0
    if b_B == "b":
        number_prefix = binary_prefixes[prefix_index] + b_B
        prefix_value = binary_values[prefix_index]
    else:
        number_prefix = decimal_prefixes[prefix_index] + b_B
        prefix_value = decimal_values[prefix_index]
    return [number_prefix, prefix_value]


print("Translate the following numbers...")
for n in range(1, 11):
    print("{}. {} to {}".format(n, generate_number()[0], generate_random_prefix()[0]))
