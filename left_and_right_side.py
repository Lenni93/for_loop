number = int(input())
left_side = 0
right_side = 0

for i in range(number):
    left_side += int(input())

for i in range(number):
    right_side += int(input())

if left_side == right_side:
    print(f"Yes, sum = {left_side}")
else:
    print(f"No, diff = {abs(left_side - right_side)}")
