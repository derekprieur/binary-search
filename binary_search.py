import random
import time

# Implement binary search algorithm!

# We will prove binary search is faster than naive searching

# naive search: scanning entire list and ask if its equal to the target
# if yes, return the index
# if no, then return -1


def naive_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1


# binary search uses divide and conquer!
# we will leverage the fact that our list is sorted
def binary_search(list, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(list) - 1

    if high < low:
        return -1

    midpoint = (low + high) // 2

    if list[midpoint] == target:
        return midpoint
    elif list[midpoint] > target:
        # remove half of list
        return binary_search(list, target, low, midpoint - 1)
    else:
        # remove half of list
        return binary_search(list, target, midpoint + 1, high)


if __name__ == "__main__":
    # list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    # target = 10
    # print(naive_search(list, 19))
    # print(binary_search(list, 19))

    length = 10000
    # build a sorted list of length 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3 * length, 3 * length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start) / length, "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start) / length, "seconds")
