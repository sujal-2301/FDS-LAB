#include <iostream>
using namespace std;

struct SLLNode *createSLL(int cnt, struct SLLNode *head);
void displaySLL(struct SLLNode *head);

void A_U_B();
void A_int_B();
void A_Min_B();
void B_Min_A();
int U_Min_A_U_B();

struct SLLNode
{
    char data;
    struct SLLNode *next;

} *headU, *headA, *headB;

int main()
{
    int no;
    int numVanilla, numButterscotch;

    headU = headA = headB = NULL;

    cout << "\n\n\t Enter number of Students of SE Comp : ";
    cin >> no;
    headU = createSLL(no, headU);
    cout << "\n";
    displaySLL(headU);

    cout << "\n\n\t Enter number of Students who like Vanilla Icecreme: ";
    cin >> numVanilla;
    headA = createSLL(numVanilla, headA);
    cout << "\n";
    displaySLL(headA);

    cout << "\n\n\t Enter number of Students who like Butterscotch Icecreme: ";
    cin >> numButterscotch;
    headB = createSLL(numButterscotch, headB);
    cout << "\n";
    displaySLL(headB);

    cout << "\n\n ----------------Input Sets:--------------------";

    cout << "\n\n Set 'U': ";
    displaySLL(headU);

    cout << "\n\n Set 'A': ";
    displaySLL(headA);

    cout << "\n\n Set 'B': ";
    displaySLL(headB);

    cout << "\n\n -------------------Output Sets:-------------------";

    int selection;
    char choice = 'y';
    while (choice == 'y' || choice == 'Y')
    {
        cout << "\n\n1. Set of students who like both vanilla and butterscotch\n";
        cout << "2. Set of students who like either vanilla or butterscotch but "
                "not both\n";
        cout << "3. Number of students who like neither vanilla nor butterscotch\n";
        cout << "4. Exit the program\n";
        cout << "---------------------------------------\n";
        cout << "\n\n Select Option:";
        cin >> selection;
        cout << '\n';

        switch (selection)
        {
        case 1:
            A_int_B();
            break;

        case 2:
            cout << "Set of students who like either vanilla or butterscotch or "
                    "not both are : ";
            A_Min_B();
            B_Min_A();
            break;

        case 3:

            cout << U_Min_A_U_B();
            break;

        case 4:
            choice = 'n';
            cout << "Thank you for using the program!";
            break;
        }
    }

    cout << "\n\n";
    return 0;
}

//.........................................................Function to create
// Linked List as Sets.

struct SLLNode *createSLL(int cnt, struct SLLNode *head)
{
    int i;
    struct SLLNode *p, *newNode;

    for (i = 0; i < cnt; i++)
    {
        newNode = new (struct SLLNode); //  1. DMA

        cout << "\n\t Enter Student Initial: "; //  2. Data & Address Assignment
        cin >> newNode->data;
        newNode->next = NULL;

        if (head == NULL) //  3. Add node in the list
        {
            head = newNode;
            p = head;
        }
        else
        {
            p->next = newNode;
            p = p->next;
        }
    }

    return head;
}
//...............................................Function to display Linked
// Lists as Sets.

void displaySLL(struct SLLNode *head)
{
    struct SLLNode *p;

    p = head;
    while (p != NULL)
    {
        cout << "  " << p->data;
        p = p->next;
    }
}
//................................................Function for Set A U B .
void A_U_B()
{
    int i, j;
    char a[10];
    struct SLLNode *p, *q;

    i = 0;     // Index of Resultant Array
    p = headA; // pointer to Set 'A'
    q = headB; // pointer to Set 'B'

    while (p != NULL && q != NULL)
    {
        if (p->data == q->data)
        {
            a[i] = p->data;
            i++;
            p = p->next;
            q = q->next;
        }
        else
        {
            a[i] = p->data;
            i++;
            p = p->next;
        }
    }
    if (p == NULL) // Set 'A' copied completely
    {
        while (q != NULL) // Copy remaining elements of Set 'B'
        {
            a[i] = q->data;
            i++;
            q = q->next;
        }
    }

    if (q == NULL) // Set 'B' copied completely
    {
        while (p != NULL) // Copy remaining elements of Set 'A'
        {
            a[i] = p->data;
            i++;
            p = p->next;
        }
    }

    cout << "\n\n\t Set A U B: ";
    for (j = 0; j < i; j++)
        cout << " " << a[j];
}
//................................................Function for Set A ^ B .

void A_int_B()
{
    int i, j;
    char a[10];
    struct SLLNode *p, *q;

    i = 0;     // Index of Resultant Array
    p = headA; // pointer to Set 'A'

    while (p != NULL)
    {
        q = headB; // pointer to Set 'B'
        while (q != NULL)
        {
            if (p->data == q->data)
            {
                a[i] = p->data;
                i++;
            }
            q = q->next;
        }
        p = p->next;
    }
    cout << "Set of students who like both vanilla and butterscotch : \n";
    cout << "\t Set A ^ B: ";
    for (j = 0; j < i; j++)
        cout << " " << a[j];
}
//................................................Function for Set A - B .

void A_Min_B()
{
    int i, j, flag;
    char a[10];
    struct SLLNode *p, *q;

    i = 0;     // Index of Resultant Array
    p = headA; // pointer to Set 'A'

    while (p != NULL)
    {
        flag = 0;
        q = headB; // pointer to Set 'B'
        while (q != NULL)
        {
            if (p->data == q->data)
            {
                flag = 1;
            }
            q = q->next;
        }
        if (flag == 0)
        {
            a[i] = p->data;
            i++;
        }
        p = p->next;
    }
    cout << "\n\n";
    for (j = 0; j < i; j++)
        cout << " " << a[j];
}

//................................................Function for Set B - A.

void B_Min_A()
{
    int i, j, flag;
    char a[10];
    struct SLLNode *p, *q;

    i = 0;     // Index of Resultant Array
    q = headB; // pointer to Set 'B'

    while (q != NULL)
    {
        flag = 0;
        p = headA; // pointer to Set 'A'
        while (p != NULL)
        {
            if (q->data == p->data)
            {
                flag = 1;
            }
            p = p->next;
        }
        if (flag == 0)
        {
            a[i] = q->data;
            i++;
        }
        q = q->next;
    }

    for (j = 0; j < i; j++)
        cout << " " << a[j];
    cout << "\n\n";
}

//................................................Function for Set U - (A U B).

int U_Min_A_U_B()
{
    int count = 0;
    int i, j, flag;
    char a[10];
    struct SLLNode *p, *q, *r;

    i = 0;     // Index of Resultant Array
    p = headU; // pointer to Set 'U'

    while (p != NULL)
    {
        flag = 0;
        q = headA; // pointer to Set 'A'
        r = headB; // pointer to Set 'B'
        while (q != NULL)
        {
            if (p->data == q->data)
            {
                flag = 1;
            }
            q = q->next;
        }
        while (r != NULL)
        {
            if (p->data == r->data)
            {
                flag = 1;
            }
            r = r->next;
        }
        if (flag == 0)
        {
            a[i] = p->data;
            i++;
        }
        p = p->next;
    }

    cout << "\n\n\t Set U - (A U B): ";
    for (j = 0; j < i; j++)
    {
        cout << " " << a[j];
        count++;
    }
    cout << '\n';
    cout << " Number of students who like neither vanilla nor butterscotch : ";
    return count;
}
