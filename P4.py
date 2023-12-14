# Linear search

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


# Sentinel Linear Search
# just removes the for loop parameter check in each iteration , nothing too fancy
def sentinel_search(arr, n, key):
    last = arr[n - 1]  # Last element of the array
    arr[n - 1] = key  # Element to be searched is placed at the last index
    i = 0
    while (arr[i] != key):
        i += 1
    arr[n - 1] = last  # Put the last element back
    if ((i < n - 1) or (arr[n - 1] == key)):
        return i
    else:
        return -1


def print_menu():
    print("\nSearch Operations Menu:")
    print("a) Linear Search")
    print("b) Sentinel Linear Search")
    print("c) Exit")


# Input student roll numbers who attended the training program
student_roll_numbers = []
num_students = int(
    input("Enter the number of students who attended the training program: "))

print("Enter roll numbers of students (press Enter after each roll number): ")
for _ in range(num_students):
    roll_number = int(input())
    student_roll_numbers.append(roll_number)

while True:
    print("\nRoll Numbers of Students who attended the training program:",
          student_roll_numbers)
    print_menu()
    choice = input("Enter your choice (a, b, c): ").lower()

    if choice == 'a':
        search_key = int(
            input("Enter the roll number to search using Linear Search: "))
        result = linear_search(student_roll_numbers, search_key)
        if result != -1:
            print(f"Roll number {search_key} found at index {result}")
        else:
            print(f"Roll number {search_key} not found")
    elif choice == 'b':
        search_key = int(
            input("Enter the roll number to search using Sentinel Search: "))
        result = sentinel_search(student_roll_numbers, len(
            student_roll_numbers), search_key)
        if result != -1:
            print(f"Roll number {search_key} found at index {result}")
        else:
            print(f"Roll number {search_key} not found")
    elif choice == 'c':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")
