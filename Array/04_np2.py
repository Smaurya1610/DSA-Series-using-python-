import numpy as np

array1 = np.array([4, 23, 56, 8, 9, 80, 34, 24])

print(array1)
def function(array1):
    # dtype=str   kevel aik charector value ko store karega   so we use <U3  unicode string max charector 3

    array2 = np.array([], dtype="<U3")
    N = len(array1)
    for i in range(0, N):
        if array1[i] % 4 == 0:
            array2 = np.insert(array2, i, "Yes")
        else:
            array2 = np.insert(array2, i, "No")

    return array2


result = function(array1)

print(result)
