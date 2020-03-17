import math

numbers = [4, 5, 7, 9, 25, 1, 22]

# i = 0
#
# largestNumber = -math.inf
# for i in range(len(numbers)-1):
#     if numbers[i] > numbers[i+1] & numbers[i] > largestNumber:
#         largestNumber = numbers[i]
#     elif numbers[i] < numbers[i+1] & numbers[i+1] > largestNumber:
#         largestNumber = numbers[i+1]
# print(largestNumber)

largestNumber = numbers[0]

for number in numbers:
    if number > largestNumber:
        largestNumber = number
print(largestNumber)
