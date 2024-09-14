import random

#heapify
def heapify(array: list[int], numberOfElements: int, currentIndex: int):
  largestIndex = currentIndex
  leftIndex = 2 * currentIndex + 1
  rightIndex = 2 * currentIndex + 2

  if leftIndex < numberOfElements and array[largestIndex] < array[leftIndex]:
    largestIndex = leftIndex

  if rightIndex < numberOfElements and array[largestIndex] < array[rightIndex]:
    largestIndex = rightIndex

  if largestIndex != currentIndex:
    array[currentIndex], array[largestIndex] = array[largestIndex], array[currentIndex]
    heapify(array, numberOfElements, largestIndex)

#heapSort
def heapSort(array: list[int]):
  numberOfElements = len(array)
  for currentIndex in range(numberOfElements//2 - 1, -1, -1):
        heapify(array, numberOfElements, currentIndex)

  for currentIndex in range(numberOfElements-1, 0, -1):
        array[currentIndex], array[0] = array[0], array[currentIndex]  # swap
        heapify(array, currentIndex, 0)

# generateArray will generate the corresponding array (e.g reverse sorted array)
def generateArray(numberOfElements: int, isSort: bool, sortIncreasing: bool) -> list[int]:
  array = [random.randint(0, 200) for _ in range(0, numberOfElements)]
  if (isSort):
    if sortIncreasing:
      array.sort()
    else:
      array.sort(reverse= True)

  return array

# printArray will print all the elements in the array
def printArray(array: list[int]):
    for i in range(len(array)):
        print(array[i], end=" ")
    print("\n")

def runningSort():
  array = generateArray(numberOfElements=10, isSort=False,sortIncreasing=False)
  print("Before sorting")
  printArray(array)
  heapSort(array)
  print("After sorting ")
  printArray(array)