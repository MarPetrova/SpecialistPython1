items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]

brands = []
for key in items:
    brands.append(key["brand"])
print("Товары на складе представлены брэндами: ", set(brands))

max_price = items[0]
for key in items:
    if key["price"] > max_price["price"]:
        max_price=key
print("На складе самый дорогой товар брэнда(ов): ", f"{max_price['brand']}")
