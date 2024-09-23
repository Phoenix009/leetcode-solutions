class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
        def get_char_freq(s):
            frq = [0 for i in range(26)]
            for alpha in s:
                if not alpha.isalpha(): continue
                frq[ord(alpha.lower()) - ord('a')] += 1
            return frq
    
        is_completing = lambda src, ref: all(ref[i] >= src[i] for i in range(26))

        src_frq = get_char_freq(licensePlate)
        ref_frq = [get_char_freq(s) for s in words]
    
        res = None
        res_length = float('inf')
        for word, frq in zip(words, ref_frq):
            if is_completing(src_frq, frq):
                if len(word) < res_length:
                    res_length = len(word)
                    res = word

        return res
