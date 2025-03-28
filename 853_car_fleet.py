class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True, key=lambda item: item[0])

        stack = []
        for pos, speed in cars:
            if not stack: stack.append(target // speed)
            else: 
                time = target // speed
                if time > stack[-1]: stack.append(time)

        return len(stack)
