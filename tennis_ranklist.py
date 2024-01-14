count_tournament = int(input())
begin_point = int(input())
final_point = 720
won_point = 2000
average_point = 1200
qty_wins = 0
points = 0
for i in range(count_tournament):
    tournament = input()
    if tournament == "W":
        qty_wins += 1
        points += won_point
    if tournament == "F":
        points += average_point
    if tournament == "SF":
        points += 720
else:
    pass

perc_wins = (qty_wins / count_tournament) * 100
aver_tour = points / count_tournament
final = begin_point + points


print(f'Final points: {final}')
print(f'Average points: {int(aver_tour)}')
print(f'{perc_wins:.2f}%')
