import random

class MaxHeap:
  def __init__(self) -> None:
    self.heap = []

  # Time complexity: O(log n) (worst case is O(n) when resizie the array for appending the elements
  # https://stackoverflow.com/a/77296220)
  def insert(self, priority: int) -> None:
    self.heap.append(priority)
    self.heapifyUp(len(self.heap) - 1)

  # heapifyUp will compare the current elements with the parent node and swap it if the
  # parent node is larger. Moreover, continue to do the same operations with the parent node.
  # Time complexity: O(log n)
  def heapifyUp(self, currentIndex: int) -> None:
    while currentIndex > 0:
      parentIndex = (currentIndex - 1) // 2
      if self.heap[currentIndex] > self.heap[parentIndex]:
        self.heap[currentIndex], self.heap[parentIndex] = self.heap[parentIndex], self.heap[currentIndex]
        currentIndex = parentIndex
      else:
        break

  # Time complexity: O(log n)
  def remove(self):
    if len(self.heap) == 0:
      return None

    if len(self.heap) == 1:
      return self.heap.pop()

    largestPriority = self.heap[0]
    self.heap[0] = self.heap.pop()
    self.heapifyDown(0)
    return largestPriority

  # heapifyDown will compare the current node with the leaf node
  # to replace the current node if the leaf node is larger.
  # Then, heapifyDown the leaf node operation if the current node is smaller
  # Time complexity: O(log n)
  def heapifyDown(self, currentIndex: int):
    while currentIndex * 2 + 1 < len(self.heap):
      largestIndex = currentIndex
      leftNodeIndex = currentIndex * 2 + 1
      rightNodeIndex = currentIndex * 2 + 2

      if leftNodeIndex < len(self.heap) and self.heap[leftNodeIndex] > self.heap[largestIndex]:
          largestIndex = leftNodeIndex

      if rightNodeIndex < len(self.heap) and self.heap[rightNodeIndex] > self.heap[largestIndex]:
          largestIndex = rightNodeIndex

      if self.heap[currentIndex] < self.heap[largestIndex]:
          self.heap[currentIndex], self.heap[largestIndex] = self.heap[largestIndex], self.heap[currentIndex]
          currentIndex = largestIndex
      else:
          break

  # Time complexity: O(n)
  def printHeap(self) -> None:
    for i in range(len(self.heap)):
        print(self.heap[i], end=" ")
    print("\n")

class PriorityQueue:
  def __init__(self):
    self.priorityQueue = MaxHeap()

  # insert will add each element into a max heap by using the priority to determine
  # which element should be the root node (largest prirotiy)
  # Time complexity: O(log n)
  def insert(self, priority: int):
    self.priorityQueue.insert(priority)

  # extractMax will extract the root node as the largest priority element,
  # replace it with the last element, and perform heapify down to
  # ensure max heap maintains its structure
  # Time complexity: O(log n)
  def extractMax(self):
    return self.priorityQueue.remove()

  # isEmpty will check if the
  # Time complexity: O(1)
  def isEmpty(self) -> bool:
    return len(self.priorityQueue.heap) == 0

  # changePriority will change the priortiy of the current index
  # if the priority is higher than the current index's priority,
  # then perform a heapify up to maintain the heap structure and vice versa
  # Time complexity: O(log n)
  def changePriority(self, index: int, priority: int) -> None:
    oldPriority = self.priorityQueue.heap[index]
    self.priorityQueue.heap[index] = priority
    if priority > oldPriority:
      self.priorityQueue.heapifyUp(index)
    else:
      self.priorityQueue.heapifyDown(index)

  # printPriorityQueue will print all the elements in the heap
  # Time complexity: O(n)
  def printPriorityQueue(self):
    self.priorityQueue.printHeap()

def generatePriorityQueue(numberOfElements: int) -> PriorityQueue:
  pq = PriorityQueue()
  for _ in range(0, numberOfElements):
    pq.insert(random.randint(0, 200))

  return pq

def runningSchedulingSystem():
  pq = generatePriorityQueue(numberOfElements=10)
  print("Priority Queue :")
  pq.printPriorityQueue()
  print("Node with largest priority :" ,  pq.extractMax())
  print("Node with 2nd largest priority :" ,  pq.extractMax())
  pq.changePriority(1, 220)
  print("Priority Queue after changing priority :")
  pq.printPriorityQueue()
  print("After changing priority with node 1, node with largest priority:" ,  pq.extractMax())
  print("Is Priority Queue empty:", pq.isEmpty() )
