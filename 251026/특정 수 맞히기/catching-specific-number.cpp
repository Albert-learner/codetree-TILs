#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n;
    cin >> n;

    while(n != 25)
    {
        if(n > 25)
            cout << "Lower" << endl;
        else
            cout << "Higher" << endl;
            
        cin >> n;
    }
    cout << "Good";
    return 0;
}