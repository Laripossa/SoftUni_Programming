lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
current_loss = 1
expenses = 0
broken_shields = 0

for fight in range(lost_fights_count):
    if current_loss % 2 == 0:
        expenses += helmet_price
    if current_loss % 3 == 0:
        expenses += sword_price
        if current_loss % 2 == 0:
            expenses += shield_price
            broken_shields += 1
    if broken_shields == 2:
        expenses += armor_price
        broken_shields = 0

    current_loss += 1

print(f"Gladiator expenses: {expenses:.2f} aureus")

