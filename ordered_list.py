class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):  # item = freq
        self.item = item
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.item)

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of
    list)'''
    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           DO NOT have an attribute to keep track of size'''
        self.head = Node(None)
        self.tail = None

    def is_empty(self):
        '''Returns True if OrderedList is empty. MUST have O(1) performance'''
        return self.head.item is None and self.tail is None

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list) and returns True.
           If the item is already in the list, do not add it again and return False.
           MUST have O(n) average-case performance'''

        if self.in_list(item):
            return False

        new_node = Node(item)
        current_node = self.head.next
        while current_node is not None and current_node.item < item:
            current_node = current_node.next
        if current_node is not None:
            new_node.prev = current_node.prev
            new_node.next = current_node
            current_node.prev = new_node
            if new_node.prev is not None:
                new_node.prev.next = new_node
            else:
                self.head.next = new_node
        else:
            if self.tail is not None:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            else:
                self.head.next = new_node
                self.tail = new_node
        return True

    def in_list(self, item):
        curr_node = self.head.next
        while curr_node is not None:
            if curr_node.item == item:
                return True
            curr_node = curr_node.next
        return False

    def remove(self, item):
        '''Removes the first occurrence of an item from OrderedList. If item is removed (was
        in the list) returns True.  If item was not removed (was not in the list) returns False
        MUST have O(n) average-case performance'''
        if self.is_empty():
            raise IndexError
        curr = self.head.next
        while curr is not None:
            if curr.item == item:
                if curr.prev is not None:
                    curr.prev.next = curr.next
                else:
                    self.head.next = curr.next
                if curr.next is not None:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev
                return True
            curr = curr.next
        return False

    def index(self, item):
        '''Returns index of the first occurrence of an item in OrderedList (assuming head of
        list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        if not self.in_list(item):
            return None

        index = 0
        curr = self.head
        while curr.next.item != item:
            index += 1
            curr = curr.next
        return index

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        if self.is_empty() or index < 0 or index >= self.size():
            raise IndexError
        curr = self.head.next
        for i in range(index):
            curr = curr.next
        temp = curr.item
        if curr.prev is not None:
            curr.prev.next = curr.next
        else:
            self.head.next = curr.next
        if curr.next is not None:
            curr.next.prev = curr.prev
        else:
            self.tail = curr.prev
        return temp

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        return self.search_helper(item, self.head.next)

    def search_helper(self, item, node):
        if node is None:
            return False
        if node.item == item:
            return True
        return self.search_helper(item, node.next)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        outlist = []
        curr = self.head.next
        while curr.next:
            outlist.append(curr.item)
            curr = curr.next
        outlist.append(curr.item)
        return outlist

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using
        recursion

           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        return self.python_list_reversed_helper(self.python_list())

    def python_list_reversed_helper(self, l):
        if len(l) <= 1:
            return l
        else:
            tail = self.python_list_reversed_helper(l[1:])
            return tail + [l[0]]

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        return self.size_helper(self.head.next)

    def size_helper(self, node):
        if node is None:
            return 0
        return 1 + self.size_helper(node.next)