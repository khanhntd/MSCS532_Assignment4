from sort import mergeSort, quickSort
import random

# heapify will build the max-heap based on the current node
# compared to its leaf node and heapify at each level
def heapify(array: list[int], numberOfElements: int, currentIndex: int) -> None:
  largestIndex = currentIndex
  leftNodeIndex = 2 * currentIndex + 1
  rightNodeIndex = 2 * currentIndex + 2

  if leftNodeIndex < numberOfElements and array[largestIndex] < array[leftNodeIndex]:
    largestIndex = leftNodeIndex

  if rightNodeIndex < numberOfElements and array[largestIndex] < array[rightNodeIndex]:
    largestIndex = rightNodeIndex

  if largestIndex != currentIndex:
    array[currentIndex], array[largestIndex] = array[largestIndex], array[currentIndex]
    heapify(array, numberOfElements, largestIndex)

# heapSort will sort based on the following steps:
# Step 1: Build a max heap using heapify
# Step 2: The root node is the largest element and it is the first element.
# Therefore, we will remove the largest element by swapping it with the last element
# and heapify again in order to replace the root node with the second largest element
# https://www.programiz.com/dsa/heap-sort
# Time complexity: O(n log n)
# Space complexity: O (log n)
def heapSort(array: list[int]) -> None:
  numberOfElements = len(array)
  # Step 1: Build a max heap
  for currentIndex in range(numberOfElements//2 - 1, -1, -1):
        heapify(array, numberOfElements, currentIndex)
  # Remove the largest element iteratively and heapify to replace the root node
  # with the second largest element
  for maxElement in range(numberOfElements-1, 0, -1):
        array[maxElement], array[0] = array[0], array[maxElement]
        heapify(array, maxElement, 0)

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
def printArray(array: list[int]) -> None:
    for i in range(len(array)):
        print(array[i], end=" ")
    print("\n")

def runningSort() -> None:
  array = generateArray(numberOfElements=10, isSort=False,sortIncreasing=False)
  print("Before sorting")
  printArray(array)
  heapSort(array)
  #mergeSort(array)
  #quickSort(array)
  print("After sorting ")
  printArray(array)