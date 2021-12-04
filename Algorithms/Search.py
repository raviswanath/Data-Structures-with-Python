# Linear search

def linear_search(data, target):
    for i in data:
        if i == target:
            return True
    return False


def binary_search(data, target):
    low = 0
    high = len(data) - 1

    while high > low:
        mid = (high + low)//2
        if data[mid] == target:
            return True
        elif data[mid] > target:
            low = mid - 1
        else:
            high = mid + 1
    return False
