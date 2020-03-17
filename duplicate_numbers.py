numbers = [2, 2, 5, 6, 5, 4, 3, 1, 4, 5]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

