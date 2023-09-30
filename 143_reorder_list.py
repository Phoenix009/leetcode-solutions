# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        def iter_list(head):
            if head:
                yield head
                yield from iter_list(head.next)

        def reorder(nodes):
            head, tail = 0, len(nodes) - 1
            while head <= tail:
                if head == tail: yield nodes[head]
                else:
                    yield nodes[head]
                    yield nodes[tail]
                    head += 1
                    tail -= 1

        nodes = [node.val for node in iter_list(head)]

        for node, val in zip(iter_list(head), reorder(nodes)):
            node.val = val



