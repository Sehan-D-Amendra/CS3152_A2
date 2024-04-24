import numpy as np
import time


#BubbleSort

def bubbleSort(numofelts):
    arr = np.random.randint(1000, size=(numofelts))
    start_time = time.time()
    n = len(arr)


    for i in range(n - 1):
        swap = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if swap == False:
            end_time = time.time()

    end_time = time.time()
    print("Bubble Sort \t " + str(end_time - start_time))


#SelectionSort

def selectionSort(numofelts):
    arr = np.random.randint(1000, size=(numofelts))
    start_time = time.time()
    n = len(arr)

    for i in range(n - 1):
        min_int = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_int]:
                min_int = j
                arr[i], arr[min_int] = arr[min_int], arr[i]

    end_time = time.time()
    print("Selection Sort \t " + str(end_time - start_time))

    return arr


# insertionSort

def insertionSort(numofelts):
    arr = np.random.randint(1000, size=(numofelts))
    start_time = time.time()
    n = len(arr)

    for i in range(1, n):
        key = arr[i]

        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    end_time = time.time()
    print("Insertion Sort \t " + str(end_time - start_time))

    return arr


# mergeSort

def mergeSortInit(numofelts):
    arr = list(np.random.randint(1000, size=(numofelts)))
    start_time = time.time()
    mergeSort(arr)
    end_time = time.time()
    print("Merge Sort \t " + str(end_time - start_time))


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# QuickSort

def quickSortInit(numofelts):
    arr = list(np.random.randint(1000, size=(numofelts)))
    size = len(arr)

    start_time = time.time()
    quickSort(arr, 0, size - 1)
    end_time = time.time()
    print("Quick Sort \t " + str(end_time - start_time))


# function to perform quicksort
def quickSort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quickSort(array, p, q - 1)
        quickSort(array, q + 1, r)


# function to find the partition position
def partition(array, p, r):

    pivot = array[r]


    i = p - 1


    for j in range(p, r):
        if array[j] <= pivot:
            i = i + 1

            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[r]) = (array[r], array[i + 1])
    return i + 1


#CountingSort

def countingSort(numofelts):
    arr = np.random.randint(1000, size=numofelts)
    start_time = time.time()

    max_element = max(arr)
    count = [0] * (max_element + 1)

    for i in arr:
        count[i] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    output = [0] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1


    for i in range(len(arr)):
        arr[i] = output[i]

    end_time = time.time()
    print("Counting Sort \t\t", end_time - start_time)
    return arr


def algorithmRunningTimeCalculator(numofelts):
    print("\n---------------------------------------------")
    print("Algorithmn \t\t Running Time at " + str(numofelts) + " elements")
    bubbleSort(numofelts)
    selectionSort(numofelts)
    insertionSort(numofelts)
    mergeSortInit(numofelts)
    quickSortInit(numofelts)
    countingSort(numofelts)
    print("\n----------------------------------------------")



# for 100000 elements bubble,insertion and selection Sort takes a long time

def algorithmRunningTimeCalculator_100000(numofelts):
    print("\n-----------------------------------------------")
    print("Algorithmn \t\t Running Time at " + str(numofelts) + " elements")
    mergeSortInit(numofelts)
    quickSortInit(numofelts)
    countingSort(numofelts)
    print("\n------------------------------------------------")



algorithmRunningTimeCalculator(10)
algorithmRunningTimeCalculator(100)
algorithmRunningTimeCalculator(1000)
algorithmRunningTimeCalculator(10000)
algorithmRunningTimeCalculator_100000(100000)



