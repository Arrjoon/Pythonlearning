"""Like a stack, the queue is a linear data structure that stores items in a First In First Out (FIFO) manner. With a queue, the least recently added item is removed first. A good example of a queue is any queue of consumers for a re
source where the consumer that came first is served first.

Operations associated with queue are: 

Enqueue: Adds an item to the queue. If the queue is full, then it is said to be an Overflow condition – Time Complexity : O(1)
Dequeue: Removes an item from the queue. The items are popped in the same order in which they are pushed. If the queue is empty, then it is said to be an Underflow condition – Time Complexity : O(1)
Front: Get the front item from queue – Time Complexity : O(1)
Rear: Get the last item from queue – Time Complexity : O(1)
"""

queue = []
queue.append('a')
queue.append('b')
queue.append('c')
print("Queue Before removing the queue")
print(queue)
queue.pop(0)
queue.pop(0)
queue.pop(0)
print("\n Queue After removing elements ")
print(queue)