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
        self.length = len(self)
