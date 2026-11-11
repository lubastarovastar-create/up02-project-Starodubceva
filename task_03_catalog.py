catalog = [
    {"name": "Кроссовки", "price": 8500,  "qty": 3},
    {"name": "Ботинки",   "price": 15000, "qty": 1},
    {"name": "Туфли",     "price": 12000, "qty": 5},
    {"name": "Сандалии",  "price": 4500,  "qty": 8},
    {"name": "Кеды",      "price": 6000,  "qty": 2},
]

print("Каталог товаров:")

total_sum = 0

for i, item in enumerate(catalog, start=1):
    name  = item["name"]
    price = item["price"]
    qty   = item["qty"]
    cost  = price * qty
    total_sum += cost

    # выравниваем название по ширине 11 символов (по самой длинной — «Кроссовки»)
    print(f"{i}. {name:<11} — {price} × {qty} = {cost} руб.")

print("-" * 30)
print(f"Итого: {total_sum} руб.")