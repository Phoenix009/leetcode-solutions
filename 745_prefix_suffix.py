class WordFilter:

    def __init__(self, words: List[str]):
        def insert_trie(root, word, val):
            curr_node = root
            for alpha in word:
                if alpha not in curr_node:
                    curr_node[alpha] = {'val': -1}
                curr_node = curr_node[alpha]
                curr_node['val'] = val
            curr_node['val'] = val

        self.trie = {}

        for index, word in zip(range(len(words), -1, -1), reversed(words)):
            for i in range(len(word)):
                insert_trie(self.trie, f"{word[i:]}-{word}", index)

    def f(self, pref: str, suff: str) -> int:
        def query_trie(root, subs):
            curr_node = root
            for alpha in subs:
                if alpha not in curr_node:
                    return -1
                curr_node = curr_node[alpha]
            if curr_node['val']: return curr_node['val']
            return -1

        return query_trie(self.trie, f"{suff}-{pref}")

