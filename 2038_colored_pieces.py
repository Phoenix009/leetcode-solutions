class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        def run_length(nums):
            if not nums: return None, 0
            count = 1
            current = nums[0]
            for num in nums[1:]:
                if num != current:
                    yield current, count
                    current, count = num, 1
                else: count += 1
            yield current, count

        alice_moves, bob_moves = 0, 0
        for char, count in run_length(colors):
            if char == 'A': alice_moves += max(0, count - 2)
            if char == 'B': bob_moves += max(0, count - 2)

        return alice_moves > bob_moves



