from sys import maxsize

number = int(input())
max_number = -maxsize
min_number = maxsize

for _ in range(number):
    current = int(input())

    if current > max_number:
        max_number = current

    if current < min_number:
        min_number = current

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
