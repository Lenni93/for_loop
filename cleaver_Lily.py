ages = int(input())
price_laundry = float(input())
price_per_toy = int(input())
total_toys = 0
total_money = 0
current_birthday_money = 0

for birthday in range(1, ages + 1):
    if birthday % 2 == 0:
        current_birthday_money += 10
        total_money += current_birthday_money - 1
    else:
        total_toys += 1
total_money += total_toys * price_per_toy
diff = abs(total_money - price_laundry)
if total_money >= price_laundry:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")
