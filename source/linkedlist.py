#!python

# this creates our nodes, which is necessary for our linked lists
class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        O(n): we are looping over the entire list, making our dependency our input"""
        length = 0
        node = self.head
        while node != None:
            length += 1
            node = node.next
        return length

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) this is a constant function because there are no loops, or recursion"""
        node = Node(item)
        if self.tail != None:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) no loops or recursion"""
        node = Node(item)
        if self.head != None:
            node.next = self.head
        else:
            self.tail = node
        self.head = node

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case: O(n) having one loop, and being dependent on input 
        Worst case: O(n^2) looping over list then looping until quality equals true"""
        node = self.head
        while node != None:
            if quality(node.data):
                return node.data
            node = node.next
        return None 

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(n+2, takes a while to loop over the entire list and set new values
        Worst case running time: 0(n^2) loop inside of loops"""
        if self.head != None:
            previous_node = None
            node = self.head
            while node != None:
                if node.data == item:
                    if previous_node != None:
                        previous_node.next = node.next
                    else:
                        self.head = node.next
                    if node.next == None:
                        self.tail = previous_node
                    return
                previous_node = node
                node = node.next
        raise ValueError('Item not found: {}'.format(item))

    def replace(self, item, new):
        node = self.head
        if node != None:
            node = Node(new)



def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
