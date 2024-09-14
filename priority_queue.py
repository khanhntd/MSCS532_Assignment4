import random

class MaxHeap:
  def __init__(self) -> None:
    self.heap = []

  def insert(self, priority: int) -> None:
    self.heap.append(priority)
    self.heapifyUp(len(self.heap) - 1)

  def heapifyUp(self, currentIndex: int) -> None:
    while currentIndex > 0:
      parentIndex = (currentIndex - 1) // 2
      if self.heap[currentIndex] > self.heap[parentIndex]:
        self.heap[currentIndex], self.heap[parentIndex] = self.heap[parentIndex], self.heap[currentIndex]
        currentIndex = parentIndex
      else:
        break

  def remove(self):
    if len(self.heap) == 0:
      return None

    if len(self.heap) == 1:
      return self.heap.pop()

    largestPriority = self.heap[0]
    self.heap[0] = self.heap.pop()
    self.heapifyDown(0)
    return largestPriority

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

  def printHeap(self) -> None:
    for i in range(len(self.heap)):
        print(self.heap[i], end=" ")
    print("\n")

class PriorityQueue:
  def __init__(self):
    self.priorityQueue = MaxHeap()

  def insert(self, priority: int):
    self.priorityQueue.insert(priority)

  def extractMax(self):
    return self.priorityQueue.remove()

  def isEmpty(self) -> bool:
    return len(self.priorityQueue) == 0

  def changePriority(self, index: int, priority: int) -> None:

    oldPriority = self.priorityQueue.heap[index]
    self.priorityQueue.heap[index] = priority
    if priority > oldPriority:
      self.priorityQueue.heapifyUp(index)
    else:
      self.priorityQueue.heapifyDown(index)

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
