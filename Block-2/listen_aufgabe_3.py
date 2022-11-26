def sum_all(numbers: list):
    total = 0
    for n in numbers:
        total += n
    return total


def multiply_all(numbers: list):
    res = 1
    for n in numbers:
        res *= n
    return res


def get_bigger(numbers: list):
    bigger = numbers[0]
    for n in numbers:
        bigger = n if n > bigger else bigger
    return bigger


def get_smaller(numbers: list):
    smaller = numbers[0]
    for n in numbers:
        smaller = n if n < smaller else smaller
    return smaller


def is_empty(numbers: list):
    return True if len(numbers) <= 0 else False


def index_of_smaller(numbers: list):
    return numbers.index(get_smaller(numbers))


def double_list(numbers: list):
    new_list = []
    for n in numbers:
        new_list.append(n * 2)
    return new_list


def count_two_ziffer(numbers: list):
    counter = 0
    for n in numbers:
        counter += 1 if 10 <= n <= 99 else 0
    return counter


def delete_evens(numbers: list):
    new_list = []
    for n in numbers:
        if n % 2 != 0:
            new_list.append(n)
    return new_list


def all_positive(numbers: list):
    is_positive = True
    for n in numbers:
        if n < 0:
            return False
    return True


def ratio_positive_negative_numbers(numbers: list):
    pos = 0
    neg = 0
    for n in numbers:
        if n >= 0:
            pos += 1
        else:
            neg += 1
    if pos == neg:
        return "There are equal amount of positive numbers as negative numbers"
    elif pos > neg:
        return "There are more positive numbers"
    else:
        return "There are more negative numbers"


def has_duplicates(numbers: list):
    for n in numbers:
        if numbers.count(n) >= 2:
            return True
    return False


def remove_duplicates(numbers: list):
    to_remove = []
    for n in numbers:
        times = numbers.count(n) - 1  # we hold one value
        el = [n, times]
        if times >= 2 and el not in to_remove:
            to_remove.append(el)
    for arr in to_remove:
        n = arr[0]
        times_to_remove = arr[1]
        for x in range(0, times_to_remove):
            numbers.remove(n)
    return to_remove


def matching_elements(list1: list, list2: list):
    for el1 in list1:
        if el1 in list2:
            return True
    return False


def get_second_smaller(numbers: list):
    smaller = get_smaller(numbers)
    new_list = numbers.copy()
    new_list.remove(smaller)
    return get_smaller(new_list)


def order_list(numbers: list):
    numbers.sort()
    return numbers


numbers_list = [5, 5, 5, 5, 2, 9, 13, 16, 27, 1, 67, 12, 56]
no_match = [100, 200, 300]
match = [431236, 23243, 67, 6234, 12]

print("Remove duplicates: ", remove_duplicates(numbers_list))
print("The sum of the hole liste is: ", sum_all(numbers_list))
print("The biggest number is: ", get_bigger(numbers_list))
print("The multiplication off all numbers is: ", multiply_all(numbers_list))
print("The smaller number is: ", get_smaller(numbers_list))
print("Testing on an empty list: ", is_empty([]))
print("Is our list empty: ", is_empty(numbers_list))
print("The index of the smaller: ", index_of_smaller(numbers_list))
print("Doubling the list: ", double_list(numbers_list))
print("Two ziffer numbers: ", count_two_ziffer(numbers_list))
print("Deleting evens: ", delete_evens(numbers_list))
print("Are all positive: ", all_positive(numbers_list))
print(ratio_positive_negative_numbers(numbers_list))
print("Has duplicates: ", has_duplicates(numbers_list))
print("Comparing with no match: ", matching_elements(numbers_list, no_match))
print("Comparing with match: ", matching_elements(numbers_list, match))
print("The second smaller number is: ", get_second_smaller(numbers_list))
print("Sorted list: ", order_list(numbers_list))
