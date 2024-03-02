# Name: Danielle McBride
# OSU Email: mcbridda@oregonstate.edu
# Course: CS261 - Data Structures
# Assignment: 2
# Due Date: 2/5/24
# Description: Create multiple methods of the DynamicArray class. Resize - change
# capacity of the array, Append - add new value to array, Insert at Index - add
# a value to a specific location in the array, Remove at Index - removes a value
# at a specific location in the array, Slice - Remove a specific range of items from
# the array, Merge - Combine two arrays, Map - Create new array derived from map_func, 
# Filter - filter specific items in the array into a new array, Reduce - reduce the 
# of the array, Find Mode - find the mode of the array and return the frequency.
 

from static_array import StaticArray


class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._size = 0
        self._capacity = 4
        self._data = StaticArray(self._capacity)

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self._size) + "/" + str(self._capacity) + ' ['
        out += ', '.join([str(self._data[_]) for _ in range(self._size)])
        return out + ']'

    def __iter__(self):
        """
        Create iterator for loop
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self._index = 0
        return self

    def __next__(self):
        """
        Obtain next value and advance iterator
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        try:
            value = self[self._index]
        except DynamicArrayException:
            raise StopIteration

        self._index += 1
        return value

    def get_at_index(self, index: int) -> object:
        """
        Return value from given index position
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        return self._data[index]

    def set_at_index(self, index: int, value: object) -> None:
        """
        Store value at given index in the array
        Invalid index raises DynamicArrayException
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if index < 0 or index >= self._size:
            raise DynamicArrayException
        self._data[index] = value

    def __getitem__(self, index) -> object:
        """
        Same functionality as get_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.get_at_index(index)

    def __setitem__(self, index, value) -> None:
        """
        Same functionality as set_at_index() method above,
        but called using array[index] syntax
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.set_at_index(index, value)

    def is_empty(self) -> bool:
        """
        Return True is array is empty / False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size == 0

    def length(self) -> int:
        """
        Return number of elements stored in array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._size

    def get_capacity(self) -> int:
        """
        Return the capacity of the array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self._capacity

    def print_da_variables(self) -> None:
        """
        Print information contained in the dynamic array.
        Used for testing purposes.
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        print(f"Length: {self._size}, Capacity: {self._capacity}, {self._data}")

    # -----------------------------------------------------------------------

    def resize(self, new_capacity: int) -> None:
    # Resize an array

        if new_capacity <= 0 or new_capacity < self.length():
            return

        new_arr = StaticArray(new_capacity)

        # Copy elements to the new array
        for i in range(self.length()):
            new_arr.set(i, self.get_at_index(i))

        # Update capacity and array
        self._capacity = new_capacity
        self._data = new_arr

        pass

    def append(self, value: object) -> None:
    # Add a value to array
        
        curr_len = self.length()
        curr_cap = self.get_capacity()

        # When array length = array capacity double capacity
        if curr_len == curr_cap:
            new_cap = curr_cap * 2
            self.resize(new_cap)

        # Update array and size
        self._data.set(curr_len, value)
        self._size += 1

        pass

    def insert_at_index(self, index: int, value: object) -> None:
    # Add a value at specific index
        
        curr_cap = self.get_capacity()
        curr_len = self.length()

        # Return error if out of bounds
        if index < 0 or index > curr_len:
            raise DynamicArrayException

        # Resize if size = capacity
        if curr_len == curr_cap:
            self.resize(curr_cap * 2)

        # Shift elements to make space
        for i in range(curr_len, index, -1):
            self._data.set(i, self.get_at_index(i-1))

        # Insert value in array at index
        self._data.set(index, value)
        self._size += 1

        pass

    def remove_at_index(self, index: int) -> None:
    # Remove a value at specific index
        
        curr_cap = self.get_capacity()
        curr_len = self.length()

        # Return error if out of bounds
        if index < 0 or index >= curr_len or curr_len == 0:
            raise DynamicArrayException

       # Update capacity and resize the array
        if curr_cap > 10 and curr_len < curr_cap / 4:
            self.resize((curr_len * 2) if (curr_len * 2) > 10 else 10)

        # Shift elements to make space
        for i in range(index, curr_len - 1, 1):
            self._data[i] = self._data[i + 1]
        self._size -= 1

        pass

    def slice(self, start_index: int, size: int) -> "DynamicArray":
    # Pull values from array between a specific range
        
        curr_len = self.length()
        new_arr = DynamicArray()

        # Return error if out of bounds
        if start_index < 0 or start_index >= curr_len or size < 0 or size > curr_len:
            raise DynamicArrayException

        if start_index + size > curr_len:
            raise DynamicArrayException

        # Pull out values and insert into new array
        for i in range(start_index, min(start_index + size, curr_len)):
            new_arr.append(self[i])

        return new_arr

        pass

    def merge(self, second_da: "DynamicArray") -> None:
    # Append items from new array into original array
        new_len = second_da.length()

        # Iterate through new array and add values to original array
        for i in range(new_len):
            new_val = second_da.get_at_index(i)
            self.append(new_val)

        pass

    def map(self, map_func) -> "DynamicArray":
    # Create a new array w/ values derived by the map_func
        
        new_arr = DynamicArray()
        curr_len = self.length()

        # Use map_func to get new values and add into an array
        for i in range(curr_len):
            val = self.get_at_index(i)
            map_val = map_func(val)
            new_arr.append(map_val)

        return new_arr

        pass

    def filter(self, filter_func) -> "DynamicArray":
    # Filters the original array and creates a new array with those values
        
        new_arr = DynamicArray()
        curr_len = self.length()

        # Pulls out desired values and inserts them into new array
        for i in range(curr_len):
            fil_val = self.get_at_index(i)
            if filter_func(fil_val):
                new_arr.append(fil_val)

        return new_arr

        pass

    def reduce(self, reduce_func, initializer=None) -> object:
    # Create a new array w/ values derived by reduce_func
        
        curr_len = self.length()

        if self.is_empty():
            return initializer

        # Sets final initializer and index
        if initializer is None:
            fin_val = self.get_at_index(0)
            index = 1
        else:
            fin_val = initializer
            index = 0

        for i in range(index, curr_len):
            fin_val = reduce_func(fin_val, self.get_at_index(i))

        return fin_val

        pass

def find_mode(arr: DynamicArray) -> tuple[DynamicArray, int]:
# Returns the values in the array that appear most and the count of times seen
    
    arr_len = arr.length()
    mode_arr = DynamicArray()
    max_cnt = 1
    curr_cnt = 1
    last_val = arr[arr_len - 1]

    # Update count if the values are the same
    for i in range(0, arr_len - 1 ):
        curr_val = arr[i]
        next_val = arr[i + 1]
        if curr_val == next_val:
            curr_cnt += 1
        else:
            # Create new array and update values if new mode detected
            if curr_cnt > max_cnt:
                mode_val = curr_val
                max_cnt = curr_cnt
                mode_arr = DynamicArray()
                mode_arr.append(mode_val)
            # If current item has same count as mode adds current item to mode array
            elif curr_cnt == max_cnt:
                mode_arr.append(curr_val)
            curr_cnt = 1

    # Check the last item in the array and add to mode if applicable
    if curr_cnt > max_cnt:
        max_cnt = curr_cnt
        mode_val = last_val
        mode_arr = DynamicArray()
        mode_arr.append(mode_val)
    elif curr_cnt == max_cnt:
        mode_arr.append(last_val)

    return mode_arr, max_cnt

    pass


# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print("\n# resize - example 1")
    da = DynamicArray()

    # print dynamic array's size, capacity and the contents
    # of the underlying static array (data)
    da.print_da_variables()
    da.resize(8)
    da.print_da_variables()
    da.resize(2)
    da.print_da_variables()
    da.resize(0)
    da.print_da_variables()

    print("\n# resize - example 2")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    print(da)
    da.resize(20)
    print(da)
    da.resize(4)
    print(da)

    print("\n# append - example 1")
    da = DynamicArray()
    da.print_da_variables()
    da.append(1)
    da.print_da_variables()
    print(da)

    print("\n# append - example 2")
    da = DynamicArray()
    for i in range(9):
        da.append(i + 101)
        print(da)

    print("\n# append - example 3")
    da = DynamicArray()
    for i in range(600):
        da.append(i)
    print(da.length())
    print(da.get_capacity())

    print("\n# insert_at_index - example 1")
    da = DynamicArray([100])
    print(da)
    da.insert_at_index(0, 200)
    da.insert_at_index(0, 300)
    da.insert_at_index(0, 400)
    print(da)
    da.insert_at_index(3, 500)
    print(da)
    da.insert_at_index(1, 600)
    print(da)

    print("\n# insert_at_index example 2")
    da = DynamicArray()
    try:
        da.insert_at_index(-1, 100)
    except Exception as e:
        print("Exception raised:", type(e))
    da.insert_at_index(0, 200)
    try:
        da.insert_at_index(2, 300)
    except Exception as e:
        print("Exception raised:", type(e))
    print(da)

    print("\n# insert at index example 3")
    da = DynamicArray()
    for i in range(1, 10):
        index, value = i - 4, i * 10
        try:
            da.insert_at_index(index, value)
        except Exception as e:
            print("Cannot insert value", value, "at index", index)
    print(da)

    print("\n# remove_at_index - example 1")
    da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    print(da)
    da.remove_at_index(0)
    print(da)
    da.remove_at_index(6)
    print(da)
    da.remove_at_index(2)
    print(da)

    print("\n# remove_at_index - example 2")
    da = DynamicArray([1024])
    print(da)
    for i in range(17):
        da.insert_at_index(i, i)
    print(da.length(), da.get_capacity())
    for i in range(16, -1, -1):
        da.remove_at_index(0)
    print(da)

    print("\n# remove_at_index - example 3")
    da = DynamicArray()
    print(da.length(), da.get_capacity())
    [da.append(1) for i in range(100)]  # step 1 - add 100 elements
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 68 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 3 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 4 - remove 1 element
    print(da.length(), da.get_capacity())
    [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 6 - remove 1 element
    print(da.length(), da.get_capacity())
    da.remove_at_index(0)  # step 7 - remove 1 element
    print(da.length(), da.get_capacity())

    for i in range(14):
        print("Before remove_at_index(): ", da.length(), da.get_capacity(), end="")
        da.remove_at_index(0)
        print(" After remove_at_index(): ", da.length(), da.get_capacity())

    print("\n# remove at index - example 4")
    da = DynamicArray([1, 2, 3, 4, 5])
    print(da)
    for _ in range(5):
        da.remove_at_index(0)
        print(da)

    print("\n# slice example 1")
    da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    da_slice = da.slice(1, 3)
    print(da, da_slice, sep="\n")
    da_slice.remove_at_index(0)
    print(da, da_slice, sep="\n")

    print("\n# slice example 2")
    da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    print("SOURCE:", da)
    slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3), (6, 1), (6, -1)]
    for i, cnt in slices:
        print("Slice", i, "/", cnt, end="")
        try:
            print(" --- OK: ", da.slice(i, cnt))
        except:
            print(" --- exception occurred.")

    print("\n# merge example 1")
    da = DynamicArray([1, 2, 3, 4, 5])
    da2 = DynamicArray([10, 11, 12, 13])
    print(da)
    da.merge(da2)
    print(da)

    print("\n# merge example 2")
    da = DynamicArray([1, 2, 3])
    da2 = DynamicArray()
    da3 = DynamicArray()
    da.merge(da2)
    print(da)
    da2.merge(da3)
    print(da2)
    da3.merge(da)
    print(da3)

    print("\n# map example 1")
    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    print(da.map(lambda x: x ** 2))

    print("\n# map example 2")


    def double(value):
        return value * 2


    def square(value):
        return value ** 2


    def cube(value):
        return value ** 3


    def plus_one(value):
        return value + 1


    da = DynamicArray([plus_one, double, square, cube])
    for value in [1, 10, 20]:
        print(da.map(lambda x: x(value)))

    print("\n# filter example 1")


    def filter_a(e):
        return e > 10


    da = DynamicArray([1, 5, 10, 15, 20, 25])
    print(da)
    result = da.filter(filter_a)
    print(result)
    print(da.filter(lambda x: (10 <= x <= 20)))

    print("\n# filter example 2")


    def is_long_word(word, length):
        return len(word) > length


    da = DynamicArray("This is a sentence with some long words".split())
    print(da)
    for length in [3, 4, 7]:
        print(da.filter(lambda word: is_long_word(word, length)))

    print("\n# reduce example 1")
    values = [100, 5, 10, 15, 20, 25]
    da = DynamicArray(values)
    print(da)
    print(da.reduce(lambda x, y: (x // 5 + y ** 2)))
    print(da.reduce(lambda x, y: (x + y ** 2), -1))

    print("\n# reduce example 2")
    da = DynamicArray([100])
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))
    da.remove_at_index(0)
    print(da.reduce(lambda x, y: x + y ** 2))
    print(da.reduce(lambda x, y: x + y ** 2, -1))

    print("\n# find_mode - example 1")
    test_cases = (
        [1, 1, 2, 3, 3, 4],
        [1, 2, 3, 4, 5],
        ["Apple", "Banana", "Banana", "Carrot", "Carrot",
         "Date", "Date", "Date", "Eggplant", "Eggplant", "Eggplant",
         "Fig", "Fig", "Grape"]
    )

    for case in test_cases:
        da = DynamicArray(case)
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}\n")

    case = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    da = DynamicArray()
    for x in range(len(case)):
        da.append(case[x])
        mode, frequency = find_mode(da)
        print(f"{da}\nMode: {mode}, Frequency: {frequency}")