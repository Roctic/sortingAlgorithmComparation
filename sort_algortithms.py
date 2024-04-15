# Insertion Sort Algorithm
# array: array to be sorted (ascendent order)
def insertionSort(array):
    for i in range(1, len(array)): #On²
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j] :
                array[j + 1] = array[j]
                j -= 1
        array[j + 1] = key  
        
# Another sort algorithms must be included in this file...  

#Algoritm bubbleSort

def bubbleSort(array):
     for i in range(len(array)-1, 0, -1): #On²
          for c in range(i):
                if array[c]>array[c+1]:
                     aux=array[c]
                     array[c]= array[c+1]
                     array[c+1]= aux
        
#Algoritm selectionSor

def selectionSort(Array): #On²
    n = len(Array)
    for i in range(n):
        index = i
        for j in range(i + 1, n):
            if Array[j] < Array[index]:
                index = j
        Array[i], Array[index] = Array[index], Array[i]
    return Array
    
#Algoritm quicksort

def quicksort(array):
    if len(array) <= 1:
        return array
    
    index = [(0, len(array) - 1)]

    while index:
        start, end = index.pop()
        if start >= end:
            continue
        pivot = array[end]
        i = start - 1
        for j in range(start, end):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]

        array[i + 1], array[end] = array[end], array[i + 1]

        index.append((start, i))
        index.append((i + 2, end))
    
    return array

#Algoritm merge sort
   
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

   
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result
                
