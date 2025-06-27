class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

# Session 1, Advanced set 1
# Problem 1: Selective DNA Deletion
# keep m nodes, skip n nodes, repeat
# edge cases
# reaching end of list while skipping nodes
def edit_dna_sequence(dna_strand: Node, m: int, n: int) -> Node:
    
    # when m == 0, keep none
    if m == 0:
        return None
    # traverse list with current
    current = dna_strand
    while current:
        for _ in range(m-1): # keep node
            if not current:
                return dna_strand
            current = current.next
        # node before skip
        before_skip = current
        current = current.next
        before_skip.next = None
        for _ in range(n): # skip n nodes
            if not current:
                return dna_strand
            current = current.next
        # set the .next of the node before skip
        before_skip.next = current
    return dna_strand # return head


def cycle_length(protein: Node) -> list[str]:
    # use some kind of hashing to store the Node object
    seen: set[Node] = set()
    curr = protein
    # linked list traversal
    while curr not in seen:
        # store the nodes we've seen in a set
        if not curr:
            # no cycle
            return []
        seen.add(curr)
        curr = curr.next
    
    # curr is at the start of the cycle
    start_of_cycle = curr
    res: list[str] = [curr.value]
    curr = curr.next
    # traverse again   goes from start -> break when at start again
    while curr is not start_of_cycle:
        # store the nodes we've seen in a set
        res.append(curr.value)
        curr = curr.next
    return res
