#include <iostream>
#include <string>
#include <sstream>
#include <limits>
using namespace std;

class addressbook
{
private:
    string fname = "";
    string lname = "";
    string address = "";
    int phonenum, id;

public:
    void setname(string name)
    {
        stringstream temp(name);
        temp >> fname >> lname;
    };
    void setphone(int pn)
    {
        phonenum = pn;
    }
    void setaddress(string astr)
    {
        address = astr;
    }
    void setid(int a)
    {
        id = a;
    }
    string getfname()
    {
        return fname;
    }
    string getlname()
    {
        return lname;
    }
    string getaddress()
    {
        return address;
    }
    int getphone()
    {
        return phonenum;
    }
    int getid()
    {
        return id;
    }
};

void addnew(addressbook arr[50], int n, int &ptr)
{
    for (int i = 0; i < n; i++)
    {
        string name, astr, input;
        int pn;
        cout << "This is new member number: " << i + 1 << "\n";
        cout << "Name: \n";
        getline(cin, name);

        cout << "Phone number: \n";
        getline(cin, input);
        // Validate and convert phone number input
        stringstream phoneStream(input);
        if (phoneStream >> pn)
        {
            // Valid integer input
            cout << "Address: \n";
            getline(cin, astr);

            arr[ptr].setname(name);
            arr[ptr].setphone(pn);
            arr[ptr].setaddress(astr);
            arr[ptr].setid(ptr);
            ptr++;
        }
        else
        {
            // Invalid input, display error message
            cout << "Invalid phone number. Please try again.\n";
            i--; // Repeat the current iteration
        }
    }
}

void editbyid(addressbook &x)
{
    string name, a, input;
    int pn;
    cout << x.getfname() << " " << x.getlname() << "\n";
    cout << "Name: \n";
    getline(cin, name);

    cout << x.getphone() << "\n";
    cout << "Phone number: \n";
    getline(cin, input);
    pn = stoi(input);

    cout << x.getaddress() << "\n";
    cout << "Address: \n";
    getline(cin, a);

    x.setname(name);
    x.setphone(pn);
    x.setaddress(a);
}

void searchbyname(addressbook arr[50], string n, int ptr)
{
    int flag = 0;
    for (int i = 0; i < ptr; i++)
    {
        if (arr[i].getfname().find(n) != std::string::npos || arr[i].getlname().find(n) != std::string::npos)
        {
            flag = 1;
            cout << arr[i].getid() << "\n";
            cout << arr[i].getfname() << " " << arr[i].getlname() << "\n";
            cout << arr[i].getphone() << "\n";
            cout << arr[i].getaddress() << "\n\n";
        }
    }
    if (flag == 0)
    {
        cout << "Sorry, no such person.\n";
    }
}

void deletebyid(addressbook arr[50], int n, int &ptr)
{
    addressbook temp[50];
    int j = 0;
    for (int i = 0; i < ptr - 1; i++)
    {
        if (i != n)
        {
            temp[j] = arr[i];
            temp[j].setid(j);
            j++;
        }
    }
    for (int i = 0; i < 50; i++)
    {
        arr[i] = temp[i];
    }
    ptr--;
}

int main()
{
    addressbook arr[50];
    char choice = ' ';
    int ptr = 0, n;
    string s;
    while (choice != 'Q')
    {
        cout << "1. Add new member to address book\n";
        cout << "2. Search member info in the address book by name\n";
        cout << "3. Edit member info in the address book\n";
        cout << "4. View the address book\n";
        cout << "5. Delete record by id\n";
        cout << "Q. Exit\n";
        cout << "User input: ";
        cin >> choice;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        switch (choice)
        {
        case '1':
            cout << "How many records you want to add?\n";
            cin >> n;
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            addnew(arr, n, ptr);
            break;

        case '2':
            cout << "Search address book by name:\n";
            getline(cin, s);
            searchbyname(arr, s, ptr);
            break;

        case '3':
            cout << "Edit address book info with id:\n";
            cin >> n;
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            editbyid(arr[n]);
            break;

        case '4':
            for (int i = 0; i < ptr; i++)
            {
                cout <<"ID: "<< arr[i].getid() << "\n";
                cout <<"Name: "<<arr[i].getfname() << " " << arr[i].getlname() << "\n";
                cout <<"Phone number: "<<arr[i].getphone() << "\n";
                cout <<"Address: "<<arr[i].getaddress() << "\n\n";
            }
            break;

        case '5':
            int x;
            cout << "The id of the record: \n";
            cin >> x;
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            deletebyid(arr, x, ptr);
            break;

        case 'Q':
            break;

        default:
            cout << "No such option.\n";
            break;
        }
    }

    return 0;
}
