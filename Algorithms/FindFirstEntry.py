# problem: write a function that takes an array of sorted integers and a key and
# returns the index of the first occurrence of that key from the array.

def find(A, target):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (high + low)//2
        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        else:
            if mid - 1 < 0:
                return mid
            if A[mid - 1] != target:
                return mid
            high = mid - 1
    return None


# We can also use the bisect method
import bisect

# bisect_left gives the index of first occurance of target in a sorted list
# bisect right gives the index of the last occurance + 1 of target in a sorted
# list.
# bisect defaults to bisect right


if __name__ == "__main__":
    A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    target = 108
    x = find(A, target)
    print(x)

    # to showcase the functionality of the "bisect" method.
    A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]

    # -10 is at index 1
    print(bisect.bisect_left(A, -10))

    # First occurrence of 285 is at index 6
    print(bisect.bisect_left(A, 285))
