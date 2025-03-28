def sumPrefixScores(words):
    root = {'count': 0}
    def insert(root, word):
        current_node = root
        for alpha in word:
            if alpha not in current_node: current_node[alpha] = {'count': 0}
            current_node = current_node[alpha]
            current_node['count'] += 1
        return root

    def get_score(root, words):
        score = 0
        current_node = root
        for alpha in words:
            if alpha not in current_node: return score
            current_node = current_node[alpha]
            score += current_node['count']
        return score

    for word in words:
        root = insert(root, word)
    
    res = [get_score(root, word) for word in words]
    return res


print(sumPrefixScores(["abc","ab","bc","b"]))

