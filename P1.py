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


def createSportList(sport_name):
    sport_list = []

    n = int(input(f"Enter the number of students playing {sport_name}: "))
    print(
        f"Enter the name of each student, press ENTER after each name for {sport_name}")
    for i in range(n):
        ele = input()
        sport_list.append(ele)

    print(f"The list of students playing {sport_name} is: {sport_list}")
    sport_list = removeDuplicate(sport_list)
    print(
        f"List of students playing {sport_name} after removing duplicate elements: {sport_list}")

    return sport_list


# Creating the lists for each sport
Cricket = createSportList("cricket")
Football = createSportList("football")
Badminton = createSportList("badminton")

# Creating the menu for the program
while True:
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
    elif (ch == 2):
        eCoB(Cricket, Badminton)
    elif (ch == 3):
        nCnB(Football, Cricket, Badminton)
    elif (ch == 4):
        CFnB(Cricket, Football, Badminton)
    else:
        print("Thanks for using the Program!")
        break

    yon = input("Do you wish to continue? y/n : ")
    if yon.lower() != "y":
        print("Thanks for using the Program!")
        break
