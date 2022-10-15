def solution(list_of_nums = []):
    # Check if list_of_nums is a valid input.
    if not list_of_nums or not isinstance(list_of_nums, list):
        # If list_of_nums is not a valid input return empty list.
        return []

    # Return merge sort recursive solution
    return merge_sort_recursion(list_of_nums)

def merge_sort_recursion(list_of_nums):
    # Basic case.
    if len(list_of_nums) == 1:
        return list_of_nums

    # Split the list.
    split_index = int(len(list_of_nums)/2)
    sublist_a = list_of_nums[:split_index]
    sublist_b = list_of_nums[split_index:]

    # Recursion with the sublists.
    sublist_a = merge_sort_recursion(sublist_a)
    sublist_b = merge_sort_recursion(sublist_b)

    # Return the merge of the sorted sublists.
    return merge(sublist_a, sublist_b)

def merge(sublist_a, sublist_b):
    new_list = []

    # While sublists have elements.
    while len(sublist_a)!=0 and len(sublist_b)!=0:
        # Add the lower num in the new_list.
        if sublist_a[0] > sublist_b[0]:
            transfer_value(sublist_b, new_list)
        else:
            transfer_value(sublist_a, new_list)

    # sublist_a or sublist_b is empty,
    # we can finish to add the final nums on the new list as we know that they are aleady ordered.
    while len(sublist_a)!=0:
        transfer_value(sublist_a, new_list)
    while len(sublist_b)!=0:
        transfer_value(sublist_b, new_list)

    return new_list

def transfer_value(sublist, new_list):
    new_list.append(sublist[0])
    del sublist[0]
