# Problem: find a number in the array that is closest to the target number.

def find_closest_num(A, target):
    high = len(A) - 1
    low = 0
    closest_num = None
    mid_diff = mid_diff_left = mif_diff_right = float("inf")

    # treat edge cases
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[1]

    while low <= high:
        mid = (high + low)//2

        # check to left and right of mid
        # provided mid values are in the right range
        if mid + 1 < len(A):
            mid_diff_right = abs(A[mid + 1] - target)
        if mid > 0:
            mid_diff_left = abs(A[mid - 1] - target)

        if mid_diff > mid_diff_left:
            mid_diff = mid_diff_left
            closest_num = A[mid - 1]

        if mid_diff > mid_diff_right:
            mid_diff = mid_diff_right
            closest_num = A[mid + 1]

        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
            if high < 0:
                return A[mid]
        else:
            return A[mid]
    return closest_num

if __name__ == "__main__":
    A1 = [1, 2, 4, 5, 6, 6, 8, 9]
    A2 = [2, 5, 6, 7, 8, 8, 9]

    print(find_closest_num(A1, 11))
    print(find_closest_num(A2, 4))
