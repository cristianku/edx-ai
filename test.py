import Queue

class pirla:
   def __init__(self,x):
      self.pirlavar = x


pq = Queue.PriorityQueue()
pq.put((12, pirla(100)))  # 1 is priority, 3 is data
pq.put((2, pirla(200)))  # 2 is priority, 4 is data
pq.put((10, pirla(300)))  # 2 is priority, 5 is data
print(pq.get()[1].pirlavar, str(pq))
print(pq.get(), str(pq))

