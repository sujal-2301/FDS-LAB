#include <iostream>
using namespace std;
#define MAX 10

struct queue
{
    int head;
    int tail;
    int data[MAX];
};

class Queue
{

public:
    queue q;
    Queue() { q.head = q.tail = -1; }
    void enqueue(int);
    void dequeue();
    bool isFull();
    bool isEmpty();
    void display();
};

bool Queue::isFull()
{
    if (q.tail + 1 == MAX)
    {
        return true;
    }
    return false;
}

bool Queue::isEmpty()
{
    if (q.head == q.tail)
    {
        return true;
    }
    return false;
}

void Queue::enqueue(int x) { q.data[++q.tail] = x; }

void Queue::dequeue()
{
    cout << "Dequeued element: " << q.data[++q.head] << endl;
}

void Queue::display()
{
    for (int i = q.head + 1; i <= q.tail; i++)
    {
        cout << q.data[i] << " ";
    }
}
int main()
{
    Queue obj;
    int ch, x;
    do
    {
        cout << "\n 1.Insert job\n 2.Delete job\n 3.Display\n 4.Exit\n Enter your "
                "choice : ";
        cin >> ch;
        switch (ch)
        {
        case 1:
            if (!obj.isFull())
            {
                cout << "\n Enter data : ";
                cin >> x;
                obj.enqueue(x);
            }
            else
                cout << "Queue is overflowed";
            break;
        case 2:
            if (!obj.isEmpty())
            {

                obj.dequeue();
            }
            else
            {
                cout << "\n Queue is underflowed ";
            }
            cout << "\nremaining jobs : ";
            obj.display();
            break;
        case 3:
            if (!obj.isEmpty())
            {
                cout << "\n Queue contains : ";
                obj.display();
            }
            else
                cout << "\n Queue is empty";
            break;
        case 4:
            cout << "\n Exit";
        }
    } while (ch != 4);
    return 0;
}
