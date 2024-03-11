def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def next_prime(num):
    while True:
        num += 1
        if is_prime(num):
            return num


def prime_rectangle(height, width, start):
    result = []
    prime_sum = 0
    current = start
    for _ in range(height):
        row = []
        for _ in range(width):
            prime = next_prime(current)
            row.append(prime)
            prime_sum += prime
            current = prime
        result.append(row)
    for row in result:
        print(" ".join(map(str, row)))

    print(prime_sum)


print("'''")
prime_rectangle(2, 3, 13)
print("'''")

print("  ")
print("'''")
prime_rectangle(5, 2, 1)
print("'''")
