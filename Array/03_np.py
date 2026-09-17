import numpy as np

array = np.array([10, 62, 30, 40, 50, 60])
# array = np.array([])


def middle_element(array):
    #  N=array.size
    N = len(array)
    if N == 0:
        print("Array is empty")
    elif N == 1:
        print(f"Middle element is {array[N-1]}")
    else:
        middle = N // 2 - 1
        print(f"Middle element is {array[middle]}")


middle_element(array)
