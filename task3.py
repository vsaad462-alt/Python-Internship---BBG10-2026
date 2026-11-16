numbers = [14, 52, 89, 14, 23, 67, 52, 91, 34, 89, 10, 45, 23, 78, 99]

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print(unique_numbers)