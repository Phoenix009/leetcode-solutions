"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None 
        
        curr_node = head
        while curr_node:
            new_node = Node(curr_node.val)

            new_node.next = curr_node.next
            curr_node.next = new_node

            curr_node = curr_node.next.next

        curr_node = head
        while curr_node:
            if curr_node.random:
                curr_node.next.random = curr_node.random.next
            curr_node = curr_node.next.next

        curr_node = head.next
        while curr_node.next:
            curr_node.next = curr_node.next.next
            curr_node = curr_node.next

        return head.next

