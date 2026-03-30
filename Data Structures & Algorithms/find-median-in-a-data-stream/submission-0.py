class MedianFinder:
    def __init__(self):
        self.left = []
        self.right = []
        self.left_size = 0
        self.right_size = 0

    def addNum(self, num: int) -> None:
        if self.left_size == self.right_size: # 0 == 0
            if self.right_size != 0 and self.right[0] < num:
                heapq.heappush(self.right, num)
                self.right_size += 1
            else:
                heapq.heappush(self.left, -num)
                self.left_size += 1
        elif self.left_size > self.right_size:
            if -self.left[0] > num:
                move_num = -heapq.heappop(self.left)
                heapq.heappush(self.left, -num)
                heapq.heappush(self.right, move_num)
            else:
                heapq.heappush(self.right, num)
            self.right_size += 1
        else:
            if self.right[0] < num:
                move_num = heapq.heappop(self.right)
                heapq.heappush(self.right, num)
                heapq.heappush(self.left, -move_num)
            else:
                heapq.heappush(self.left, -num)
            self.left_size += 1

    def findMedian(self) -> float:
        # [1, 2, 3, 4, 5]
        if self.right_size > self.left_size:
            return self.right[0]
        if self.left_size > self.right_size:
            return -self.left[0]
        
        return (-self.left[0] + self.right[0])/2