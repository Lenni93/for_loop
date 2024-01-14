from math import inf
total_sum = 0
max_sum = -inf

n = int(input())

for i in range(0, n):
    current_num = int(input())
    total_sum += current_num

    if current_num > max_sum:
        max_sum = current_num

if max_sum == total_sum - max_sum:
    print('Yes')
    print(f"Sum = {max_sum}")

else:
    diff = abs(max_sum - (total_sum - max_sum))
    print('No')
    print(f'Diff = {diff}')
# is the difference
#  10 is the greater number which we are using loops with another total_sum and collect them so we ve got all together 12
# and we are looking for equal by 10 which mean 3 times checking 1 by 1 = 2  + looking for 10
# and then we ve got 8 difference