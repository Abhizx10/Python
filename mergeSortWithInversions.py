"""
Program to perform mergesort for a given input list of numbers and
calculate the total count of inversions. An inversion results when
you copy the number from the right half to the final list.
"""

inversions = 0

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        leftHalf = alist[:mid]
        rightHalf = alist[mid:]
        mergeSort(leftHalf)
        mergeSort(rightHalf)
        mergeSortInv(alist,leftHalf,rightHalf)


def mergeSortInv(alist,leftHalf,rightHalf):   
    global inversions
    i,j,k = 0,0,0
    
    while i <len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            alist[k] = leftHalf[i]
            i = i+1
        else:
            alist[k] = rightHalf[j]
            inversions = inversions + len(leftHalf) -i 
            j = j+1
            k = k+1

    while i < len(leftHalf):
        alist[k] = leftHalf[i]
        i = i+1
        k = k+1

    while j < len(rightHalf):
        alist[k] = rightHalf[j]
        j = j+1
        k = k+1
if __name__ == '__main__':
    fh = open('IntegerArray.txt')
    line_list = fh.readlines()
    final_list = []
    for number in line_list:
        final_list.append(int(number.strip()))
    mergeSort(final_list)
    print(inversions)
