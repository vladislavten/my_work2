players = {
    ("Ivan", "Volkin"): (10, 5, 13),
    ("Bob", "Robbin"): (7, 5, 14),
    ("Rob", "Bobbin"): (12, 8, 2)
}

# TODO здесь писать код

lst = []

for key, value in players.items():
    lst.append(key + value)

print(lst)
