count_browser = int(input())
salary = int(input())
fines = 0
for open_tags in range(count_browser):
    website = input()
    if website == 'Facebook':
        salary -= 150
    elif website == 'Instagram':
        salary -= 100
    elif website == 'Reddit':
        salary -= 50
    if salary <= 0:
        break
if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")
