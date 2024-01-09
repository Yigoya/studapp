#include <iostream>
using namespace std;

const int MAXSIZE = 500;

class Linked_list
{
public:
    int list[MAXSIZE];
    int pos, n, i;
    void Create()
    {
        cout << "\n Enter the number of elements to be added in the list: ";
        cin >> n;
        cout << "\n Enter the array elements:\n";
        for (int i = 0; i < n; i++)
        {
            cin >> list[i];
        }
    }
    void Insert()
    {
        int data;
        cout << "enter the position: ";
        cin >> pos;
        cout << "enter the data to be inserted: ";
        cin >> data;
        if (pos == n)
        {
            cout << "Array over flow";
        }
        else if (pos < 1 || pos > n + 1)
        {
            cout << "Invalid position";
        }
        else
        {
            for (int i = n - 1; i >= pos - 1; i--)
            {
                list[i + 1] = list[i];
            }
        }
        list[pos - 1] = data;
        n = n + 1;
        Display();
    }
    void Delete()
    {
        cout << "Enter the posithin of the data to be deleted:";
        cin >> pos;
        cout << "the data deleted is:\t" << list[pos - 1];
        for (int i = pos - 1; i < n - 1; i++)
        {
            list[i] = list[i + 1];
            n = n - 1;
        }
        Display();
    }
    void Display()
    {
        for (i = 0; i < n; i++)
        {
            cout << "\t" << list[i];
        }
    }
    void Search()
    {
        int search, count = 0;
        cout << "\n Enter the element to be searched:";
        cin >> search;
        for (i = 0; i < n; i++)
        {
            if (search == list[i])
                count++;
        }
        if (count == 0)
        {
            cout << "Element not present in the list";
        }
        else
        {
            cout << "\n Element present in the list";
        }
    }
};

void menu()
{
    cout << "linked List Menu:" << endl;
    cout << "\n Array Implementation of List\n";
    cout << "\t1.create\n";
    cout << "\t2.Insert\n";
    cout << "\t3.Delete\n";
    cout << "\t4.Display\n";
    cout << "\t5.Search\n";
    cout << "\t6.Exit\n";
    cout << "\n Enter your choice:\t";
}

int main()
{
    Linked_list Link;
    int choice;
    do
    {
        menu();
        cin >> choice;
        switch (choice)
        {
        case 1:
            Link.Create();
            break;
        case 2:
            Link.Insert();
            break;
        case 3:
            Link.Delete();
            break;
        case 4:
            Link.Display();
            break;
        case 5:
            Link.Search();
            break;
        // case 6: exit(1);
        default:
            cout << ("\n Enter option between 1 - 6\n");
            break;
        }
    } while (choice < 7);
}