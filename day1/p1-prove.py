dict = [
    1721,
    979,
    366,
    299,
    675,
    1456
]

for a in dict:
    for b in dict:
        if b + a == 2020:
            print(b*a)
            break
        