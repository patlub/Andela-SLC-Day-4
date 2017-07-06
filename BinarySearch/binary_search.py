class BinarySearch(list):
    """
    Class to search for a value using binary search
    """

    def __init__(self, a, b) -> None:
        """
        Constructor for the class
        Args:
            a: length of list
            b: step
        """
        super().__init__()
        self.a = a
        self.b = b

        # Generate list and assign it to class
        for x in range(1, a + 1):
            self.append(x * b)
        self.length = a

    def search(self, value) -> dict:
        """
        Makes a search using binary search
        Args:
            value: key to search for
        Returns:
            dict: Containing number of iterations and index
        """
        count = 0
        first = 0
        last = len(self) - 1
        mid = 0
        found = False

        try:
            if value == self[first]:
                found = True
                mid = first
            elif value == self[last]:
                found = True
                mid = last
            elif value not in self:
                found = True
                mid = -1

            # Loop through the list while incrementing the count
            # the return a dictionary containing the count and
            # the index of found value.
            while first <= last and not found:
                mid = (first + last) // 2
                if self[mid] == value:
                    found = True
                else:
                    if self[mid] > value:
                        last = mid - 1
                        count += 1
                    else:
                        first = mid + 1
                        count += 1

            return {'count': count, 'index': mid}

        except:
            raise ValueError
