# problem: Given an array of nn distinct integers sorted in ascending order,
# write a function that returns a fixed point in the array. If there is not a
# fixed point, return None.

# A fixed point in an array A is an index i such that A[i] is equal to i.

def fixed_point(A):
    low = 0
    high = len(A) - 1
    index = 0

    while low <= high:
        mid = (low + high)//2
        if A[mid] < mid:
            low = mid + 1
        elif A[mid] > mid:
            high = mid - 1
        else:
            return A[mid]
    return None


if __name__ == "__main__":
    # Fixed point is 3:
    A1 = [-10, -5, 0, 3, 7]
    # Fixed point is 0:
    A2 = [0, 2, 5, 8, 17]
    # No fixed point. Return "None":
    A3 = [-10, -5, 3, 4, 7, 9]
    print(A1)
    print(fixed_point(A1))
    print(A2)
    print(fixed_point(A2))
    print(A3)
    print(fixed_point(A3))
