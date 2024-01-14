name_actor = input()
point_academy = float(input())
n = int(input())
sum_of_point = point_academy
for i in range(n):
    name_judge = input()
    point_judged = float(input())

    sum_of_point += len(name_judge) * point_judged / 2

    if sum_of_point > 1250.5:
        break

diff = 1250.5 - sum_of_point
if sum_of_point > 1250.5:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {sum_of_point:.1f}!")
else:
    print(f"Sorry, {name_actor} you need {diff:.1f} more!")