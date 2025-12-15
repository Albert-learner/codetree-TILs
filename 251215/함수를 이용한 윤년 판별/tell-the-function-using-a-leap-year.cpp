#include <iostream>

using namespace std;

int y;
bool leap_discriminate(int year);

int main() 
{
    cin >> y;

    // Please write your code here.
    if(leap_discriminate(y))
        cout << "true";
    else
        cout << "false";
    return 0;
}

bool leap_discriminate(int year)
{
    if((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
        return true;

    return false;
}