# Name: Danielle McBride
# OSU Email: mcbridda@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 5
# Due Date: 3/1/24
# Description: Implementation of a minimum heap.


from dynamic_array import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initialize a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        heap_data = [self._heap[i] for i in range(self._heap.length())]
        return 'HEAP ' + str(heap_data)

    def add(self, node: object) -> None:
        """ Add new node to heap """
        # Add node to end of array
        self._heap.append(node)

        # Get the new node index
        heap_len = self._heap.length()
        curr_index = heap_len - 1

        # Percolate up heap to maintain balance
        while curr_index > 0:
            par_index = (curr_index - 1) // 2
            if self._heap[curr_index] < self._heap[par_index]:
                self._heap[par_index], self._heap[curr_index] = self._heap[curr_index], self._heap[par_index]
                curr_index = par_index
            else:
                break

    def is_empty(self) -> bool:
        """ Return T if heap empty, else F"""

        if self._heap.length() == 0:
            return True
        else:
            return False

    def get_min(self) -> object:
        """ Returns the minimum value of the heap """

        if self.is_empty is True:
            return MinHeapException
        else:
            return self._heap[0]

    def remove_min(self) -> object:
        """ Remove minimum node"""
        if self.is_empty() is True:
            raise MinHeapException

        heap_len = self._heap.length() - 1
        last_node = self._heap[heap_len]

        self._heap.remove_at_index(heap_len)

        if not self.is_empty():
            self._heap[0] = last_node
            self._percolate_down(0)

        return last_node

    def build_heap(self, da: DynamicArray) -> None:
        """ Build a heap """

        self._heap = DynamicArray(da)
        arr_len = da.length()

        for i in range(arr_len):
            self.add(da[i])

    def size(self) -> int:
        """ Returns the size of the heap """
        return self._heap.length()

    def clear(self) -> None:
        """ Clear items from heap """

        self._heap = DynamicArray()

    def _percolate_down(self, parent: int) -> None:
        """ Percolate the item down heap to aid in balancing"""

        # Set up Pointers
        arr_len = self._heap.length()
        left_index = 2 * parent + 1
        right_index = 2 * parent + 2
        min_node = parent

        # Compare children with parent node
        if left_index < arr_len and self._heap[left_index] < self._heap[min_node]:
            min_node = left_index
        if right_index < arr_len and self._heap[right_index] < self._heap[min_node]:
            min_node = right_index

        if min_node != parent:
            self._heap[parent], self._heap[min_node] = self._heap[min_node], self._heap[parent]
            self._percolate_down(min_node)
        return

def heapsort(da: DynamicArray) -> None:
    """ Sort the items in da """

    heap = MinHeap(da)
    arr_len = da.length()

    for i in range(arr_len -1, -1, -1):
        da[i] = heap.remove_min()


# It's highly recommended that you implement the following optional          #
# function for percolating elements down the MinHeap. You can call           #
# this from inside the MinHeap class. You may edit the function definition.  #





# ------------------- BASIC TESTING -----------------------------------------


if __name__ == '__main__':

    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)

    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)

    print("\nPDF - is_empty example 1")
    print("-------------------")
    h = MinHeap([2, 4, 12, 56, 8, 34, 67])
    print(h.is_empty())

    print("\nPDF - is_empty example 2")
    print("-------------------")
    h = MinHeap()
    print(h.is_empty())

    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())

    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty() and h.is_empty() is not None:
        print(h, end=' ')
        print(h.remove_min())

    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)

    print("--------------------------")
    print("Inserting 500 into input DA:")
    da[0] = 500
    print(da)

    print("Your MinHeap:")
    print(h)
    if h.get_min() == 500:
        print("Error: input array and heap's underlying DA reference same object in memory")

    print("\nPDF - heapsort example 1")
    print("------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - heapsort example 2")
    print("------------------------")
    da = DynamicArray(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(f"Before: {da}")
    heapsort(da)
    print(f"After:  {da}")

    print("\nPDF - size example 1")
    print("--------------------")
    h = MinHeap([100, 20, 6, 200, 90, 150, 300])
    print(h.size())

    print("\nPDF - size example 2")
    print("--------------------")
    h = MinHeap([])
    print(h.size())

    print("\nPDF - clear example 1")
    print("---------------------")
    h = MinHeap(['monkey', 'zebra', 'elephant', 'horse', 'bear'])
    print(h)
    print(h.clear())
    print(h)
