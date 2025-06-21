import random

inputArray = random.sample(range(1,21), 10)

elementToFind = random.randint(1,20)
elementFound = None

print(f'Input Array: {inputArray}')

for iterator in range(0, len(inputArray)):
    if inputArray[iterator] == elementToFind:
        elementFound = iterator
        break

if elementFound!=None:
    print(f'Element {elementToFind} found at index {elementFound}')
else:
    print(f'Element {elementToFind} not found')