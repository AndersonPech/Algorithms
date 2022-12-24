#!/usr/bin/env python3 

import sys

arr = [1,2,3,4,5,6]
search = 10


def binarySearch():
    left = 0
    right = len(arr) - 1
    while (right >= left):
        mid = (left + right)//2
        if (arr[mid] == search):
            return 1
        elif (arr[mid] < search):
            left = mid + 1
        elif (arr[mid] > search):
            right = mid - 1
    return -1

if __name__ == '__main__':
    if binarySearch() == -1:
        print('Number not in array')
    else:
        print('Number is in array')
