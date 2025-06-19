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

def edit_dna_sequence(dna_strand, m, n):
    m1 = 0
    n1 = 0
    marker = None
    head = dna_strand
    while dna_strand:
        if m1 < m:
            m1 += 1
        elif m1 == m and n1 == 0:
            marker = dna_strand
        if n1 < n:
            n += 1
        elif n1 == n:
            n1 = 0
            m1 = 0
            marker.next = dna_strand.next
            dna_strand.next = None
        dna_strand = dna_strand.next
    return head


dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

print_linked_list(edit_dna_sequence(dna_strand, 2, 3))
