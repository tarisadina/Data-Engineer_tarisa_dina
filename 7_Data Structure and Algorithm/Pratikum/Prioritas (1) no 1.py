def group_numbers(numbers, target):
    groups = [[] for _ in range(target)]
    for num in numbers:
        groups[num % target].append(num)
    return groups


# [[3, 6, 9], [1, 2, 4, 5, 7, 8]]
print(group_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
# [[15, 20, 75, 30, 45], [23, 19]]
print(group_numbers([23, 15, 19, 20, 75, 30, 45], 5))
