numbers = [5, 5, 2, 1, 5, 7, 4]

numbers.append(20)  # add item at the end
print(numbers)

numbers.insert(0, 10)  # add item at given index - here: 0
print(numbers)

numbers.remove(5)  # removes item at given index
print(numbers)

numbers.pop()  # removes last item
print(numbers)

print(numbers.index(7))  # gives the index of a given item

print(50 in numbers)  # boolean which shows if numbers exist in list

print(numbers.count(5))  # how many of a given item

numbers.sort() # sort in ascending order
print(numbers)
numbers.reverse()  # reverse order
print(numbers)

numbers2 = numbers.copy() # copy into new list

numbers.clear()  # clears list
print(numbers)
