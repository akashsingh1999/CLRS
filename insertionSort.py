import random

inputArray = random.sample(range(1, 101), 15)

print(f'Input Array is: {inputArray}')

lengthOfInputArray = len(inputArray)
# 1 2 3 5 3
for iterator in range(1,lengthOfInputArray):
    key = inputArray[iterator]
    iterator2 = iterator-1
    while iterator2 >= 0 and inputArray[iterator2]>key:
        inputArray[iterator2+1] = inputArray[iterator2]
        iterator2 -= 1
    inputArray[iterator2+1] = key

print(f'Array Sorted: {inputArray}')

