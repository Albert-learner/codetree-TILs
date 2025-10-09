#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    char chr;
    cin >> chr;

    if(chr == 'S')
        cout << "Superior";
    else if(chr == 'A')
        cout << "Excellent";
    else if(chr == 'B')
        cout << "Good";
    else if(chr == 'C')
        cout << "Usually";
    else if(chr == 'D')
        cout << "Effort";
    else
        cout << "Failure";
        
    return 0;
}