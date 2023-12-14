# Insertion Sort program
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def shell_sort(arr):
    gap = len(arr) // 2

    while gap > 0:
        j = gap

        while j < len(arr):
            i = j - gap

            while i >= 0:
                if arr[i + gap] > arr[i]:
                    break
                else:
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]

                i -= gap
            j += 1
        gap //= 2
    return arr


def print_menu():
    print("\nSorting Operations Menu:")
    print("a) Insertion Sort")
    print("b) Shell Sort")
    print("c) Exit")


arr = []

while True:
    print_menu()
    choice = input("Enter your choice (a, b, c): ").lower()

    if choice == 'a':
        arr = []
        n = int(input("Enter the total number of elements in the array: "))
        for i in range(n):
            ele = float(input(f"Enter the percentage of student {i + 1}: "))
            arr.append(ele)

        print("Entered Array is:", arr)
        print("Sorted array using insertion sort is:", insertion_sort(arr)[:5])
    elif choice == 'b':
        if not arr:
            print("Please perform Insertion Sort first to populate the array.")
            continue
        print("Sorted array using shell sort is:", shell_sort(arr)[:5])
    elif choice == 'c':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")
