def oddEvenList(head):
    if not head:
        return head

    odd = []
    even = []

    current_node = head
    index = 1
    while current_node:
        next_node = current_node.next
        current_node.next = None
        if index % 2 == 0:
            even.append(current_node)
        else:
            odd.append(current_node)
        current_node = next_node
        index += 1

    for i in range(len(odd) - 1):
        odd[i].next = odd[i]+1

    for i in range(len(even) - 1):
        even[i].next = even[i]+1

    odd[-1].next = even[0]

def print_list(head):
    current_node = head
    while current_node:
        print(current_node.value)
        current_node = current_node.next



