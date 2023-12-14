# Selection Sort
def selection_sort(array):
    for ind in range(len(array)):
        min_index = ind
        for j in range(ind + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[ind], array[min_index] = array[min_index], array[ind]
    print("The sorted array using selection sort is:", array)
    print("The top five percentages of students are:", array[:5])

# Bubble Sort


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("The sorted array using bubble sort is:", arr)
    print("The top five percentages of students are:", arr[:5])


def print_menu():
    print("\nSorting Operations Menu:")
    print("a) Selection Sort")
    print("b) Bubble Sort")
    print("c) Exit")


# Input percentages of first-year students
student_percentage = []
num_students = int(input("Enter the number of students: "))

print("Enter percentages of students (press Enter after each percentage): ")
for _ in range(num_students):
    percentage = float(input())
    student_percentage.append(percentage)

while True:
    print("\nPercentages of First-Year Students:", student_percentage)
    print_menu()
    choice = input("Enter your choice (a, b, c): ").lower()

    if choice == 'a':
        selection_sorted = student_percentage[:]
        selection_sort(selection_sorted)
    elif choice == 'b':
        bubble_sorted = student_percentage[:]
        bubble_sort(bubble_sorted)
    elif choice == 'c':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")
