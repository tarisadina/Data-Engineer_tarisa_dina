def get_breads(breads, flour_stock):
    available_breads = []
    for bread in breads:
        if bread["flour"] <= flour_stock:
            available_breads.append(bread["name"])
    return available_breads


bread1 = [
    {"name": "donut", "flour": 25},
    {"name": "mini puff", "flour": 15},
    {"name": "baguette", "flour": 75},
    {"name": "cupcake", "flour": 15},
]

bread2 = [
    {"name": "pancake", "flour": 15},
    {"name": "waffle", "flour": 25},
    {"name": "bagel", "flour": 15},
    {"name": "cupcake", "flour": 15},
    {"name": "choco chips", "flour": 10},
    {"name": "mini puff", "flour": 5},
    {"name": "bread", "flour": 30},
]

print(get_breads(bread1, 100))  # ['mini puff', 'cupcake', 'donut']
# ['mini puff', 'choco chips', 'pancake', 'bagel', 'cupcake']
print(get_breads(bread2, 75))
