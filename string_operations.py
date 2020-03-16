course = 'Python for Beginners'
print(len(course)) # len - number of characters, general purpose function for counting

print(course.upper()) # methods after dot
print(course.lower())

print(course.find('P')) # returns index of first occurrence, case sensitive, -1 means none find
print(course.replace('Beginners', 'Absolute Beginners'))

print('Python' in course) #boolean if 'Python' is in string
