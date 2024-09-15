# quickSort will following the three steps:
# Step 1: Choose the pivot (last element of the array)
# Step 2: Partition the array, which includes splitting and reordering
# the array so that all elements smaller than the pivot are on the left
# and all elements larger than the pivot are on the right
# Step 3: Repeat the same for the left side and right side
# Time complexity: O(n log n) (O(n^2) when the array is sorted either in descending or ascending)
# Space complexity: O(1)
# https://en.wikipedia.org/wiki/Quicksort
def quickSort(array: list[int], low: int, high: int):
  if low > high:
    return

  # Get the pivot index for the array
  pivot = partitionArray(array, low, high)
  # Perform the same implementation (choose pivot and divide) to the left side array
  quickSort(array, low, pivot - 1)
  # Perform the same implementation (choose pivot and divide) to the right side array
  quickSort(array, pivot + 1, high)

# partitionArray will partition the array based on the pivot which can be chosen from median of median
# https://medium.com/@amit.desai03/median-of-median-on-medium-5ed518f17307; however, for simplicity, we will choose
# the last element of the array. Afterwards, return the pivot index to divide and conquer
def partitionArray(array: list[int], low: int, high: int) -> int:
  pivot = array[high]

  swapStartingIndex = low - 1
  # Partition the array based on the pivot:
  # The left side will be smaller than the pivot
  # The right side will be larger than the pivot
  for currentIndex in range(low, high):
    if array[currentIndex] < pivot:
      swapStartingIndex +=1
      array[currentIndex], array[swapStartingIndex] = array[swapStartingIndex], array[currentIndex]

  # Swap the pivot element with the next element of the array's left side
  # to divide the array into two parts completely
  array[swapStartingIndex + 1], array[high] = array[high], array[swapStartingIndex + 1]
  return swapStartingIndex + 1

# mergeSort will following the two steps:
# Step 1: Divide the array into smaller sub-arrays until each subarray contains a single element
# Step 2: Sort, merge the sub-arrays recursively
# (since we are doing decreasing order)
# Time complexity: O(nlogn)
# Space complexity: O(n)
# https://en.wikipedia.org/wiki/Merge_sort
def mergeSort(array: list[int], low: int, high: int):
  if low >= high:
    return

  middle = low + (high - low)//2

  mergeSort(array,low, middle)
  mergeSort(array,middle + 1, high)
  compareAndMerge(array, low, middle, high)


# compareAndMerge will sort the two sub-arrays (n/2), merge it
def compareAndMerge(array: list[int], low: int, middle: int, high: int):
  leftArray = array[low: middle + 1]
  rightArray = array[middle + 1: high + 1]
  leftIndex = rightIndex = 0
  startIndex = low

  while leftIndex < len(leftArray) and rightIndex < len(rightArray):
    if leftArray[leftIndex] <= rightArray[rightIndex]:
      array[startIndex] = leftArray[leftIndex]
      leftIndex +=1
    else:
      array[startIndex] = rightArray[rightIndex]
      rightIndex +=1
    startIndex +=1

  # Copy the remaining elements (either from the left or right side)
  # if there are any remaining elements on the left side or right side
  while leftIndex < len(leftArray):
    array[startIndex] =  leftArray[leftIndex]
    leftIndex+=1
    startIndex+=1

  while rightIndex < len(rightArray):
    array[startIndex] =  rightArray[rightIndex]
    rightIndex+=1
    startIndex+=1