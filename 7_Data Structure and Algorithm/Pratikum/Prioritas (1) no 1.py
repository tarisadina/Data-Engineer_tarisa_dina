def group_numbers(numbers, target):
    multiples = []
    non_multiples = []
    for num in numbers:
        if num % target == 0:
            multiples.append(num)
        else:
            non_multiples.append(num)
    return [multiples, non_multiples]


# Test Case 1
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target1 = 3
output1 = group_numbers(numbers1, target1)
print("Test Case 1:", output1)

# Test Case 2
numbers2 = [23, 15, 19, 20, 75, 30, 45]
target2 = 5
output2 = group_numbers(numbers2, target2)
print("Test Case 2:", output2)
