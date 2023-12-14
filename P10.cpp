#include <iostream>
using namespace std;
#include <string.h>
#define max 50

class Stack
{
private:
    char origStr[max];
    int top;

public:
    Stack()
    {
        top = -1;
    }
    void push(char);
    void reverse();
    void convert(char[]);
    void palindrome();
};

void Stack::push(char c)
{
    top++;
    origStr[top] = c;
    origStr[top + 1] = '\0';

    cout << endl
         << c << " is pushed into the stack";
}

void Stack::reverse()
{
    char str[max];
    cout << "\n\nReverse string is : ";

    int j = 0;
    for (int i = top; i >= 0; i--)
    {
        cout << origStr[i];  // Output the character
        str[j] = origStr[i]; // Store the character in another array or variable
        j = j + 1;           // Increment j manually
    }

    cout << endl;
}

void Stack::convert(char str[])
{
    int j, k, len = strlen(str);

    for (j = 0, k = 0; j < len; j++)
    {
        if (((int)str[j] >= 97 && (int)str[j] <= 122) || (int)str[j] >= 65 && (int)str[j] <= 90)
        {
            if ((int)str[j] <= 90)
            {
                str[k] = (char)((int)str[j] + 32); // convert upper case to lower
            }
            else
            {
                str[k] = str[j];
            }
            k++;
        }
    }
    str[k] = '\0';

    cout << endl
         << "converted String : " << str << "\n";
}

void Stack::palindrome()
{
    char str[max];
    int i, j;

    for (i = top, j = 0; i >= 0; i--, j++)
    {
        str[j] = origStr[i];
    }
    str[j] = '\0';

    if (strcmp(str, origStr) == 0)
    {
        cout << "\n\nString is palindrome";
    }
    else
    {
        cout << "\n\nString is not palindrome";
    }
}

int main()
{
    Stack stack;
    char str[max];
    int i = 0;

    cout << "\nEnter string to be reversed and check if it is a palindrome or not : \n\n";

    cin.getline(str, 50);
    stack.convert(str);

    while (str[i] != '\0')
    {
        stack.push(str[i]);
        i++;
    }

    stack.palindrome();
    stack.reverse();
}
