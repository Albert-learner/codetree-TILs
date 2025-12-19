#include <iostream>

using namespace std;

bool is_leap_year(int y);
bool is_wrong_day(int y, int m, int d);

int main() 
{
    int Y, M, D;
    cin >> Y >> M >> D;

    // Please write your code here.
    if (is_wrong_day(Y, M, D)) 
    {
        cout << -1;
    } 
    else 
    {
        if (M == 12 || M == 1 || M == 2) 
        {
            cout << "Winter";
        } 
        else if (M == 3 || M == 4 || M == 5) 
        {
            cout << "Spring";
        } 
        else if (M == 6 || M == 7 || M == 8) 
        {
            cout << "Summer";
        } 
        else if (M == 9 || M == 10 || M == 11) 
        {
            cout << "Fall";
        } 
        else 
        {
            cout << -1;
        }
    }
    return 0;
}

bool is_leap_year(int y) 
{
    if ((y % 4 == 0 && y % 100 != 0) || (y % 400 == 0))
        return true;
    return false;
}

bool is_wrong_day(int y, int m, int d) 
{
    if ((m == 4 || m == 6 || m == 9 || m == 11) && d > 30)
        return true;
    else if (m == 2 && is_leap_year(y) && d > 29)
        return true;
    else if (m == 2 && !is_leap_year(y) && d > 28)
        return true;
    else
        return false;
}