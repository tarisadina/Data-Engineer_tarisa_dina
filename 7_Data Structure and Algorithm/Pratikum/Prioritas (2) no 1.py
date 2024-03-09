def collect_chars(word, rooms):
    repetitions = rooms // len(word)
    remaining_chars = rooms % len(word)
    result = word * repetitions + word[:remaining_chars]
    return result


print(collect_chars("alta", 10))  # altaaltaal
print(collect_chars("sepulsa", 20))  # sepulsasepulsasepuls
print(collect_chars("sepulsamantap", 20))  # sepulsamantapsepulsa
