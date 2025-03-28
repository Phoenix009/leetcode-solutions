class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        from queue import PriorityQueue

        pq = PriorityQueue(nums)

        tries = 0

        while True:
            num1 = pq.get()
            if num1 >= k: break
            
            tries += 1
            num2 = pq.get()

            pq.put(num1 * 2 + num2)
        return tries


        
