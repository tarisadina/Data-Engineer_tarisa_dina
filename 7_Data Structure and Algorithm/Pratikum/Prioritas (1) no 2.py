def determine_breads(flour_stock, breads):
    available_breads = []
    for bread in breads:
        if bread['flour'] <= flour_stock:
            available_breads.append(bread['name'])
            flour_stock -= bread['flour']
    return available_breads


# Test Case 1
flour_stock1 = 100
breads1 = [
    {"name": "donut", "flour": 25},
    {"name": "mini puff", "flour": 15},
    {"name": "baguette", "flour": 75},
    {"name": "cupcake", "flour": 15}
]
output1 = determine_breads(flour_stock1, breads1)
print("Test Case 1 Output:", output1)
