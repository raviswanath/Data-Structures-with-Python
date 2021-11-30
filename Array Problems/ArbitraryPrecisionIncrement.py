# Given: An array of non-negative digits that represent a decimal integer.

# Problem: Add one to the integer. Assume the solution still works even if
# implemented in a language with finite-precision arithmetic.

# Pythonic solution
def pythonic_arbitrary_increment(A):
    x = int(''.join([str(i) for i in A])) + 1
    return [int(i) for i in str(x)]


# generic solution
def arbitrary_increment(A):
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


if __name__ == "__main__":
    test1 = pythonic_arbitrary_increment([1, 4, 9])
    test2 = pythonic_arbitrary_increment([9, 9, 9])

    test3 = arbitrary_increment([1, 4, 9])
    test4 = arbitrary_increment([9, 9, 9, 9])

    print(test1)
    print(test2)
    print(test3)
    print(test4)
