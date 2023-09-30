class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        def get_chunks(s):
            chunk, count = "", ""
            
            index = 0
            while index < len(s):
                while index < len(s) and s[index].isalpha():
                    chunk += s[index]
                    index += 1

                while index < len(s) and s[index].isnumeric():
                    count += s[index]
                    index += 1

                if count == "": count = "0"
                yield chunk, int(count)

                chunk, count = "", ""

        tape_size = 0
        for chunk, count in get_chunks(s):
            tape_size += len(chunk)
            if k > tape_size * count:
                k -= tape_size * count
            else:
                k %= tape_size
                if k == 0: return chunk[-1]
                return chunk[k-1]




