def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    ans = 0
    for i in range(1, len(flowerbed)-1):
        if flowerbed[i] == 1: continue
        if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
            ans += 1
            flowerbed[i] = 1

    return ans >= n
