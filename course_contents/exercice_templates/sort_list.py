


def bubble_sort(lst):
    """Applies a bubble sort algorithm to a list.

    Buble sort is the simplest sorting algorithm that works by repeatedly
    swapping the adjacent elements if they are in wrong order. 

    No error handling is provided on this function - we assume that the input 
    is of the Integer type

    ARGS:
        A list to be sorted

    RETURNS:
        A sorted list
    """
    return None

def strings_to_ints(lst):
    """transforms a list of strings to a list of ints

    ARGS:
        list of strings

    RETURNS:
        list of ints
    
    RAISES:
        ValueError: when the string in the list is not a number
    """
    return None

def string_to_strings(string):
    """transforms a comma-separated stting to a list of strings"""
    return None


if __name__ == '__main__':

    # INPUT:    "2, 1, 3, 4, 5"
    # OUTPUT:   [1, 2, 3, 4, 5] 

    input_string = input("Comma-separated numbers: ")

    list_of_strings = string_to_strings(input_string)
    
    list_of_ints = strings_to_ints(list_of_strings)
    
    sorted_list = bubble_sort(list_of_ints)

    print(sorted_list)

    # PROGRAM TO INTERFACE, NOT TO IMPLEMENTATION