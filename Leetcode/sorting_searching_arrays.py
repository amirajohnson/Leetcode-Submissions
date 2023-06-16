#writing all sorting and searching algorithms on arrays

def selection_sort(A):
    #select the smallest element in the array and swap it with 
    #the current leftmost element.

    for i in range(len(A)):
        min_element = min(A[i:])
        min_index = A.index(min_element)
        tmp = A[i]
        A[i] = min_element
        A[min_index] = tmp


def do_partition(A, lo, pivot_index, hi):
    pass

def quick_sort(A):
    pass

def merge_sort(A):
    pass

def binary_search(A, target):
    
    lo, hi = 0, len(A)-1
    res = -1
    while lo < hi:
        print(lo, hi)
        mid = (lo + hi)//2
        if A[mid] == target:
            return mid
        elif A[mid] > target:
            hi = mid
        elif A[mid] < target:
            lo = mid+1
    return res



    


selection_array = [1, 4, 5, 2, 3, 7, 6, 9]

selection_sort(selection_array)
print(selection_array)
print(binary_search(selection_array, 7))