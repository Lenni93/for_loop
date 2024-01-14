count_group = int(input())

group_musala = 0
group_montblanc = 0
group_kilimanjaro = 0
group_k2 = 0
group_everest = 0
total_date = 0
for num in range(count_group):
    climber = int(input())
    total_date += climber

    if climber <= 5:
        group_musala += climber
    elif climber <= 12:
        group_montblanc += climber
    elif climber <= 25:
        group_kilimanjaro += climber
    elif climber <= 40:
        group_k2 += climber
    else:
        group_everest += climber


percentage1 = (group_musala / total_date) * 100
percentage2 = (group_montblanc / total_date) * 100
percentage3 = (group_kilimanjaro / total_date) * 100
percentage4 = (group_k2 / total_date) * 100
percentage5 = (group_everest / total_date) * 100

print(f"{percentage1:.2f}%")
print(f"{percentage2:.2f}%")
print(f"{percentage3:.2f}%")
print(f"{percentage4:.2f}%")
print(f"{percentage5:.2f}%")


