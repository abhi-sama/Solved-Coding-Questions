class Node:
    def __init__(self, val=0, next=None, child=None):
        self.data = val
        self.next = next
        self.child = child
# Don't change the code above.
import heapq

def flattenLinkedList(head):
    # Custom comparison function for heapq to compare node values.
    def compare(node_pair):
        node, value = node_pair
        return value
    # Heap to store all the node value pairs.
    heap = []
    # Push the head nodes.
    pointer = head
    while pointer:
        heapq.heappush(heap, (pointer.data, pointer))
        pointer = pointer.next

    # Add child nodes while popping out the minimum.
    result = None
    while heap:
        _, temp = heapq.heappop(heap)
    
        # If the child of temp is not null, add it to the heap.
        if temp.child:
            heapq.heappush(heap, (temp.child.data, temp.child))

        if not result:
            result = temp
            pointer = temp
            pointer.next = None
        else:
            pointer.child = temp
            pointer = temp
            pointer.next = None

    return result