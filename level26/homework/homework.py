def transform_list(numbers):
    new_list = []
    for num in numbers:
        if num % 2 == 0:
            new_list.append(num // 2)
        else:
            new_list.append(num * 2)
    return new_list

print(transform_list([1, 2, 3, 4]))
print(transform_list([5, 10, 3, 5]))