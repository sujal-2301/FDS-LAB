#include <iostream>
using namespace std;

class Pizza
{
    int front, rear, q[5];

public:
    Pizza()
    {
        front = -1;
        rear = -1;
    }
    int isfull()
    {

        if ((front == 0 && rear == 4) || front == rear + 1)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
    int isempty()
    {
        if (front == -1 && rear == -1)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
    void add()
    {
        if (isfull() == 0)
        {
            cout << "\n Enter the Pizza ID : ";
            if (front == -1 && rear == -1)
            {
                front = 0;
                rear = 0;
                cin >> q[rear];
            }
            else
            {
                rear = (rear + 1) % 5;
                cin >> q[rear];
            }
            char c;
            cout << " Do you want to add another order ? ";
            cin >> c;
            if (c == 'y' || c == 'Y')
                add();
        }
        else
        {
            cout << "\n Orders are full! ";
        }
    }
    void serve()
    {
        if (isempty() == 0)
        {
            if (front == rear)
            {
                cout << "\n Order served is : " << q[front];
                front = -1;
                rear = -1;
            }
            else
            {
                cout << "\n Order served is : " << q[front];
                front = (front + 1) % 5;
            }
        }
        else
        {
            cout << "\n Orders are empty! ";
        }
    }
    void display()
    {
        if (isempty() == 0)
        {
            for (int i = front; i != rear; i = (i + 1) % 5)
            {
                cout << q[i] << " <- ";
            }
            cout << q[rear];
        }
        else
        {
            cout << "\n Orders are empty!";
        }
    }
    void check()
    {
        int ch;
        cout << "\n\n * * * * WELCOME TO PIZZA PARLOUR * * * * \n\n";
        cout << "\n 1. Add a Pizza Order\n 2. Display the Orders \n 3. Serve a "
                "pizza \n "
                "4. Exit \n Enter your choice : ";
        cin >> ch;
        switch (ch)
        {
        case 1:
            add();
            break;

        case 2:

            display();
            break;

        case 3:

            serve();
            break;

        case 4:

            exit(0);

        default:
            cout << "Invalid choice ";

            check();
        }
        char ch1;
        cout << "\n Do you want to continue? ";
        cin >> ch1;
        if (ch1 == 'y' || ch1 == 'Y')
            check();
    }
};
int main()
{
    Pizza p1;
    p1.check();
    return 0;
}