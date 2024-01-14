count_number = int(input())

p1_counter = 0
p2_counter = 0
p3_counter = 0
p4_counter = 0
p5_counter = 0
for number in range(count_number):
    current_number = int(input())
    if current_number < 200:
        p1_counter += 1
    elif current_number < 400:
        p2_counter += 1
    elif current_number < 600:
        p3_counter += 1
    elif current_number < 800:
        p4_counter += 1
    elif current_number >= 800:
        p5_counter += 1

percentage1 = p1_counter / count_number * 100
percentage2 = p2_counter / count_number * 100
percentage3 = p3_counter / count_number * 100
percentage4 = p4_counter / count_number * 100
percentage5 = p5_counter / count_number * 100
print(f'{percentage1:.2f}%')
print(f'{percentage2:.2f}%')
print(f'{percentage3:.2f}%')
print(f'{percentage4:.2f}%')
print(f'{percentage5:.2f}%')

