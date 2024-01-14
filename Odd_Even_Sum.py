number = int(input())
even_number = 0
odd_number = 0

for i in range(1, number + 1):
    current_number = int(input())

    if i % 2 == 0:
        even_number += current_number
    else:
        odd_number += current_number

if odd_number == even_number:
    print(f"Yes")
    print(f'Sum = {odd_number}')

else:
    print("No")
    print(f"Diff = {abs(odd_number- even_number)}")
