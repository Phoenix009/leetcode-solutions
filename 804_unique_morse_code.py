class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        store = dict(zip([chr(ord('a') + i) for i in range(26)], codes))

        vis = set()
        for word in words:
            code = "".join([store[alpha] for alpha in word])
            vis.add(code)

        return len(vis)
