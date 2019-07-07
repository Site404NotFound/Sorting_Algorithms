#!/usr/bin/env python3
def main():
    # Establish a list of numbers (not in order) that will be sorted
    numb_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0
                 -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

    print_list("Unsorted", numb_list)
    bubble_sort(numb_list)
    print_list("Sorted", numb_list)

def bubble_sort(numb_list):
    sort_happened = True
    while sort_happened:
        sort_happened = False
        for x in range(len(numb_list) - 1):
            if numb_list[x] > numb_list[x + 1]:
                numb_list[x], numb_list[x + 1] = numb_list[x + 1], numb_list[x]
                sort_happened = True

def print_list(version, numb_list):
    print("{}: {}".format(version, ", ".join(map(str, numb_list))))

if __name__ == '__main__':
    main()
