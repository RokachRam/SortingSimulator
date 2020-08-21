import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# this function will be used in all of the sorting algorithms
def Swap(A, i, j):
    if i != j:
        temp = A[i]
        A[i] = A[j]
        A[j] = temp


# complexity: θ(n^2)
# Bubble Sort is the simplest sorting algorithm,
# It works by repeatedly swapping the adjacent elements if they are in wrong order.
def bubbleSort(A):

    if len(A) == 1:
        return

    swapped = True
    for i in range(len(A) - 1):
        if not swapped:
            break
        swapped = False
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                Swap(A, j, j + 1)
                swapped = True
            yield A


# complexity: θ(n^2)
# The array is virtually split into a sorted and an unsorted part.
# Values from the unsorted part are picked and placed at the correct position in the sorted part.
def insertionSort(A):

    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j] < A[j - 1]:
            Swap(A, j, j - 1)
            j -= 1
            yield A



# complexity: θ(nlog(n))
# This sorting algorithm divides input array in two halves, calls itself for the two halves and then merges the two sorted halves
# It uses the "merge" function
def mergeSort(A, start, end):

    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1
    yield from mergeSort(A, start, mid)
    yield from mergeSort(A, mid + 1, end)
    yield from merge(A, start, mid, end)
    yield A

# this function is used in the mergeSort algorithm
def merge(A, start, mid, end):

    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if A[leftIdx] < A[rightIdx]:
            merged.append(A[leftIdx])
            leftIdx += 1
        else:
            merged.append(A[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(A[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(A[rightIdx])
        rightIdx += 1

    for i, sorted_val in enumerate(merged):
        A[start + i] = sorted_val
        yield A


# complexity: θ(nlog(n))
# this sorting algo picks an element as pivot and partitions the given array around the picked pivot
def quickSort(A, start, end):

    if start >= end:
        return

    pivot = A[end]
    pivotIdx = start

    for i in range(start, end):
        if A[i] < pivot:
            Swap(A, i, pivotIdx)
            pivotIdx += 1
        yield A
    Swap(A, end, pivotIdx)
    yield A

    yield from quickSort(A, start, pivotIdx - 1)
    yield from quickSort(A, pivotIdx + 1, end)

# complexity: θ(n^2)
# The selection sort algorithm sorts an array by repeatedly finding
# the minimum element from unsorted part and putting it at the beginning.
# The algorithm maintains two subarrays in a given array.
def selectionSort(A):
    if len(A) == 1:
        return

    for i in range(len(A)):
        minVal = A[i]
        minIdx = i
        for j in range(i, len(A)):
            if A[j] < minVal:
                minVal = A[j]
                minIdx = j
            yield A
        Swap(A, i, minIdx)
        yield A


if __name__ == "__main__":
    N = int(input("Enter Array size to be sorted: "))
    method_msg = "Enter sorting method:\nb -> Bubble\ni -> Insertion \nm -> Merge \
        \nq -> Quick\ns -> Selection\n"
    method = input(method_msg)
# generate random array
    A = [x + 1 for x in range(N)]
    random.seed(time.time())
    random.shuffle(A)
# determine the right generator
    if method == "b":
        title = "Bubble sort"
        generator = bubbleSort(A)
    elif method == "i":
        title = "Insertion sort"
        generator = insertionSort(A)
    elif method == "m":
        title = "Merge sort"
        generator = mergeSort(A, 0, N - 1)
    elif method == "q":
        title = "Quicksort"
        generator = quickSort(A, 0, N - 1)
    else:
        title = "Selection sort"
        generator = selectionSort(A)

    fig, ax = plt.subplots()
    ax.set_title(title)
    bar_rectangles = ax.bar(range(len(A)), A, align="edge")
    ax.set_xlim(0, N)
    ax.set_ylim(0, int(1.07 * N))
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    # to show the number of iterations on screen
    iteration = [0]

# this function is called from the animation func
    def update_fig(A, bar_rectangles, iteration):
        for rect, val in zip(bar_rectangles, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))


    animation = animation.FuncAnimation(fig, func=update_fig,
                                   fargs=(bar_rectangles, iteration), frames=generator, interval=1,
                                   repeat=False)
    plt.show()