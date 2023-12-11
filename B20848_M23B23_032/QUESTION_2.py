class StudentQueue:
    def __init__(self):
        self._queue = []

    def enqueue(self, student):
        self._queue.append(student)

    def dequeue(self):
        if self._queue:
            return self._queue.pop(0)

    def is_empty(self):
        return len(self._queue) == 0

    def size(self):
        return len(self._queue)

#Examples with output of how to implement this class, demonstrating how students join the queue, get served, and ascertain the size of the queue

student_queue = StudentQueue()


# demonstration of how students join the queue
student_queue.enqueue("Mbeiza Rachel")
student_queue.enqueue("Ankunda Mwebembezi")
student_queue.enqueue("Mokili Promise")

# demonstration of how the first student in the queue is served
student_served = student_queue.dequeue()
print(f"The student to be served is : {student_served}")

#demonstration of how we are to check whether the queue is empty or not
is_empty = student_queue.is_empty()
print(f"Is the queue empty? {is_empty}")

#demonstration of how we shall obtain the size of the queue
queue_size = student_queue.size()
print(f"The current size of the queue is: {queue_size}")

