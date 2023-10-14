items_and_price = input().split("|")
budget = float(input())
train_ticket_cost = 150
markup_percent = 1.40
purchased_price = []

for product in items_and_price:
    item, price_as_str = product.split("->")
    price = float(price_as_str)
    if item == "Clothes" and price <= 50:
        if budget >= price:
            budget -= price
            purchased_price.append(price)
    elif item == "Shoes" and price <= 35:
        if budget >= price:
            budget -= price
            purchased_price.append(price)
    elif item == "Accessories" and price <= 20.50:
        if budget >= price:
            budget -= price
            purchased_price.append(price)


profit = 0

for i in range(len(purchased_price)):
    old_price = purchased_price[i]
    new_price = (purchased_price[i] * markup_percent)
    profit += new_price - old_price
    budget += new_price
    print(f"{new_price:.2f}", end=" ")

print(f"\nProfit: {profit:.2f}")
if budget >= train_ticket_cost:
    print("Hello, France!")
else:
    print("Not enough money.")