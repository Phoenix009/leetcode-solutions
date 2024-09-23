
def insertGreatestCommonDivisors(head):
    def gcd(a, b):
        while b > 0:
            a, b = b, a%b
        return a
    
    if not head: return head
    if not head.next: return head
    
    current_node = head
    next_node = head.next
    while next_node:
        new_node = ListNode(val = gcd(current_node.val, next_node.val))
        new_node.next = next_node
        current_node.next = new_node

        current_node = current_node.next
        next_node = current_node.next

    return head
