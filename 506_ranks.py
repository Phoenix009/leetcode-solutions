class Solution:
    def findRelativeRanks(self, scores: List[int]) -> List[str]:
        store = {}
        for rank, score in enumerate(sorted(scores, reverse=True)):
            if rank == 0: store[score] = "Gold Medal"
            elif rank == 1: store[score] = "Silver Medal"
            elif rank == 2: store[score] = "Bronze Medal"
            else: store[score] = str(rank + 1)

        result = [store[score] for score in scores]
        return result


