#!/usr/bin/env python3
def main():
    # Create a list of unordered numbers
    numb_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0
                 -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
    print_list(numb_list)   # Call function to print number list
    quicksort(numb_list, 0, len(numb_list) - 1)    # Call quicksort function
    print_list(numb_list)   # Call function to print number list

def partition(numb_list, low, high):
    i = low - 1
    for x in range(low, high):
        if numb_list[x] <= numb_list[high]:
            i += 1
            numb_list[i], numb_list[x] = numb_list[x], numb_list[i]
    numb_list[i + 1], numb_list[high] = numb_list[high], numb_list[i + 1]
    return i + 1

def quicksort(numb_list, low, high):
    if low < high:
        pivot = partition(numb_list, low, high)
        quicksort(numb_list, low, pivot - 1)
        quicksort(numb_list, pivot + 1, high)

def print_list(numb_list):
    print(", ".join(map(str, numb_list)))

if __name__ == '__main__':
    main()
