# Function to compute average of the class

def average(marksInFDS):
    sum = 0
    count = 0
    for i in range(len(marksInFDS)):
        if(marksInFDS[i] != -999):   
            sum += marksInFDS[i]
            count += 1
    print("Sum of marks of students in the class is : ", sum)
    return (sum/count)


# Function to compute Highest Marks

def highestMarks(marksInFDS):
    highest = marksInFDS[0]
    for i in range(len(marksInFDS)):
        if(marksInFDS[i] > highest):
            highest = marksInFDS[i]
    return highest  

# Function to compute Lowest Marks

def lowestMarks(marksInFDS):
    
    for i in range(len(marksInFDS)):
        if(marksInFDS[i] != -999):
            lowest = marksInFDS[i]
    
    for i in range(len(marksInFDS)):
        if(marksInFDS[i] != -999 and marksInFDS[i] < lowest):
            lowest = marksInFDS[i]
    return lowest  

# Function to compute number of absent students

def absentStudents(marksInFDS):
    count = 0
    for i in range(len(marksInFDS)):
        if(marksInFDS[i] == -999):
            count += 1


# Function to display marks with highest frequency

def highFreq(arr):
    max_count = 0
    most_frequent_marks = []

    for mark in arr:
        count = arr.count(mark)
        if count > max_count:
            max_count = count
            most_frequent_marks = [mark]
        elif count == max_count and mark not in most_frequent_marks:
            most_frequent_marks.append(mark)

    print("Marks with the highest frequency:")
    for mark in most_frequent_marks:
        print(mark)

    
            
# Main function

marksInFDS = []
numberOfStudent = int(input("Enter the total number of students : "))

for i in range (numberOfStudent):
    marks = int(input("Enter the marks in FDS of student "+ str(i+1) + " : "))
    marksInFDS.append(marks)
print("Marks of students are : ",marksInFDS)

# Menu Design 

flag = True
while flag:
    print("\n*************************************Welcome******************************************\n")
    print("Marks scored in subject 'Fundamental of Data Structure' by Students in the class are stored")
    print("Choose one of the following options:\n")
    print(" 1. The average score of class ")
    print(" 2. Highest score and lowest score of class ")
    print(" 3. Count of students who were absent for the test ")
    print(" 4. Display mark with highest frequency ")
    print(" 5. Exit Program ")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Average marks of students in the class is:", average(marksInFDS))
    elif choice == 2:
        print("Highest marks in the class is:", highestMarks(marksInFDS))
        print("Lowest marks in the class is:", lowestMarks(marksInFDS))
    elif choice == 3:
        print("Number of students absent for the test:", absentStudents(marksInFDS))
    elif choice == 4:
        highFreq(marksInFDS)
    elif choice == 5:
        print("Thanks for using the Program!")
        break
    else:
        print("Invalid choice!")

    yon = input("Do you wish to continue? (y/n): ")
    if yon != 'y' and yon != 'Y' :
        print("Thanks for using the Program!")
        break
