def solution(list_of_nums=[], num_to_search=None):
    # Check if list_of_nums is a valid input.
    if not list_of_nums or not isinstance(list_of_nums, list):
        # If list_of_nums is not a valid input return -1.
        return -1

    # Check if num_to_search is a valid input.
    if not num_to_search or not isinstance(num_to_search, int):
        # If num_to_search is not a valid input return -1.
        return -1

    return binary_serach_recursion(list_of_nums, num_to_search, 0, len(list_of_nums)-1)

def binary_serach_recursion(list_of_nums, num_to_search, lower_index, upper_index):
    # Get mid_index of the list.
    mid_index = int((lower_index + upper_index)/2)

    # Basic case.
    if list_of_nums[mid_index] == num_to_search:
        return mid_index

    # Non found cases.
    if lower_index >= upper_index:
        return -1

    if list_of_nums[mid_index] < num_to_search:
        # If the num on the middle is lower than the num to search.
        # Discart lower numbers.
        lower_index = mid_index+1
    else:
        # If the num on the middle is bigger than the num to search.
        # Discart upper numbers.
        upper_index = mid_index-1

    return binary_serach_recursion(list_of_nums, num_to_search, lower_index, upper_index)
