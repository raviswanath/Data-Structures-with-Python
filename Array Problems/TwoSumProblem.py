# Problem: Given an array of integers, return True or False if the array has two
# numbers that add up to a specific target. You may assume that each input would
# have exactly one solution.

# Brute force O(n^2) solution
def two_sum_brute_force(A, target):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == target:
                return True
    return False


# O(n) solution on space and time complexity
def two_sum_hash_table(A, target):
    diff_values = {}
    for i in A:
        if i in diff_values:
            return True
        else:
            diff_values[target - i] = i
    return False


# O(nlogn) time and O(1) space solution
def two_sum_third_approach(A, target):
    A = sorted(A)
    i = 0
    j = len(A) - 1
    while i < j:
        value_sum = A[i] + A[j]
        if value_sum == target:
            return True
        elif value_sum < target:
            i += 1
        elif value_sum > target:
            j -= 1
    return False


if __name__ == "__main__":
    A = [-2, 1, 2, 4, 7, 11]
    target = 13
    print(two_sum_brute_force(A,target))
    print(two_sum_hash_table(A,target))
    print(two_sum_third_approach(A, target))
    target = 20
    print(two_sum_brute_force(A,target))
    print(two_sum_hash_table(A,target))
    print(two_sum_third_approach(A, target))
