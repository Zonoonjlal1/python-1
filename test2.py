def sum_numbers(*args):
    result = 0
    for x in args:
        result += x
    return result
print(sum_numbers(1, 2, 3, 4, 5,17))  # Output: 15