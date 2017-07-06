def find_missing(list1, list2):
    """
    Function to find extra integer between two lists
    Args:
        list1:
        list2:
    """
    # Check that both arguments are lists
    if not (isinstance(list1, list) and isinstance(list2, list)):
        raise TypeError('All arguments should be lists')

    elif not all(isinstance(item, int) for item in list1 + list2):
        return 'Lists should only contain integers'

    elif not all(item > 0 for item in list1 or list2):
        return 'Lists should not have negative values'

    else:
        # Return 0 if lists are empty
        if not list1 and not list2:
            return 0
        # Return 0 if list1 equals list2
        elif list1 == list2:
            return 0
        else:
            # Use sets to find difference between lists
            if len(list1) > len(list2):
                s = set(list1) - set(list2)
            else:
                s = set(list2) - set(list1)
                # Return value from set
            return next(iter(s))
