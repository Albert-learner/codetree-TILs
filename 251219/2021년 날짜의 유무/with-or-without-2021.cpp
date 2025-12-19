#include <iostream>
using namespace std;

int main() 
{
    int M, D;
    cin >> M >> D;

    if (M >= 1 && M <= 12) 
    {
        if (M != 2) 
        {
            if (M == 1 || M == 3 || M == 5 || M == 7 ||
                M == 8 || M == 10 || M == 12) 
            {
                if (D >= 1 && D <= 31)
                    cout << "Yes";
                else
                    cout << "No";
            } 
            else 
            {
                if (D >= 1 && D <= 30)
                    cout << "Yes";
                else
                    cout << "No";
            }
        } 
        else 
        {
            if (D >= 1 && D <= 28)
                cout << "Yes";
            else
                cout << "No";
        }
    } 
    else 
    {
        cout << "No";
    }

    return 0;
}
