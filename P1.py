# function to remove duplicate elements from the list

def removeDuplicate(lst1):
    lst = []
    for i in lst1:
        if (i not in lst):
            lst.append(i)
    return lst


# functions for set operations

def union(lst1, lst2):
    lst = lst1.copy()
    for val in lst2:
        if val not in lst:
            lst.append(val)
    return lst


def intersection(lst1, lst2):
    lst = []
    for val in lst1:
        if val in lst2:
            lst.append(val)
    return lst


def diff(lst1, lst2):
    lst = []
    for val in lst1:
        if val not in lst2:
            lst.append(val)
    return lst


def sym_diff(lst1, lst2):
    lst3 = []
    l1 = diff(lst1, lst2)
    l2 = diff(lst2, lst1)
    lst3 = union(l1, l2)
    return lst3

# function to find list of students who play both cricket and badminton


def CB(lst1, lst2):
    lst3 = intersection(lst1, lst2)
    print(" List of students who play both cricket and badminton is : ", lst3)
    # return len(lst3)


# function to find List of students who play either cricket or badminton but not both

def eCoB(lst1, lst2):
    lst3 = sym_diff(lst1, lst2)
    print("List of students who play either cricket or badminton but not both is : ", lst3)


# function to find  Number of students who play neither cricket nor badminton

def nCnB(lst1, lst2, lst3):
    lst4 = diff(lst1, union(lst2, lst3))
    print("Number of students who play neither cricket nor badminton is : ", len(lst4))


# function to find  Number of students who play cricket and football but not badminton

def CFnB(lst1, lst2, lst3):
    lst4 = diff(intersection(lst1, lst2), lst3)
    print("Number of students who play cricket and football but not badminton is : ", len(lst4))


# Creating a list of total number of students
SE_COMP = []

# Taking input for this list

n = int(input("Enter the total number of students : "))
print("Enter the name of each student , press ENTER after each name ")
for i in range(n):
    ele = input()

    SE_COMP.append(ele)
print("The original list of total students is ", str(SE_COMP))
SE_COMP = removeDuplicate(SE_COMP)
print("List of total students after removing duplicate elements is : ", str(SE_COMP))


# Creating the list of students playing Cricket

Cricket = []

# Taking input for this list

n = int(input("Enter the number of students playing cricket : "))
print("Enter the name of each student , press ENTER after each name ")
for i in range(n):
    ele = input()

    Cricket.append(ele)
print("The list of students playing cricket is ", str(Cricket))
Cricket = removeDuplicate(Cricket)
print("List of students playing cricket after removing duplicate elements is : ", str(Cricket))


# Creating the list of students playing Football

Football = []

# Taking input for this list

n = int(input("Enter the number of students playing Football : "))
print("Enter the name of each student , press ENTER after each name ")
for i in range(n):
    ele = input()

    Football.append(ele)
print("The list of students playing Football is ", str(Football))
Football = removeDuplicate(Football)
print("List of students playing Football after removing duplicate elements is : ", str(Football))


# Creating the list of students playing Badminton

Badminton = []

# Taking input for this list

n = int(input("Enter the number of students playing Badminton : "))
print("Enter the name of each student , press ENTER after each name ")
for i in range(n):
    ele = input()

    Badminton.append(ele)
print("The list of students playing Badminton is ", str(Badminton))
Badminton = removeDuplicate(Badminton)
print("List of students playing Badminton after removing duplicate elements is : ", str(Badminton))


# Creating the menu for the program

flag = 1
while flag == 1:
    print("")
    print("**********************Welcome******************************")
    print("")
    print(" In second year computer engineering class, group A student’s play cricket, \n group B students play badminton and group C students play football. ")
    print(" ")
    print(" 1. List of students who play both cricket and badminton")
    print(" 2. List of students who play either cricket or badminton but not both ")
    print(" 3. Number of students who play neither cricket nor badminton ")
    print(" 4. Number of students who play cricket and football but not badminton ")
    print(" ")

    ch = int(input("Enter your choice : "))

    if (ch == 1):
        CB(Cricket, Badminton)
        yon = input("Do you wish to continue? y/n : ")
        if (yon == "y"):
            flag = 1
        else:
            print("Thanks for using the Program!")
            flag = 0

    elif (ch == 2):
        eCoB(Cricket, Badminton)
        yon = input("Do you wish to continue? y/n : ")
        if (yon == "y"):
            flag = 1
        else:
            print("Thanks for using the Program!")
            flag = 0

    elif (ch == 3):
        nCnB(Football, Cricket, Badminton)
        yon = input("Do you wish to continue? y/n : ")
        if (yon == "y"):
            flag = 1
        else:
            print("Thanks for using the Program!")
            flag = 0

    elif (ch == 4):
        CFnB(Cricket, Football, Badminton)
        yon = input("Do you wish to continue? y/n : ")
        if (yon == "y"):
            flag = 1
        else:
            print("Thanks for using the Program!")
            flag = 0

    else:
        print("Thanks for using the Program!")
        flag = 0
