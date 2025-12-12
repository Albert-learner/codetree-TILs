#include <iostream>
#include <string>
using namespace std;

int main() 
{
    string a_str, b_str;
    cin >> a_str >> b_str;

    int min_n = 0;
    int cnts = 0;
    int n = a_str.size();

    while (cnts < n) 
    {
        if (a_str != b_str) 
        {
            a_str = a_str.back() + a_str.substr(0, n - 1);
        } 
        else 
        {
            min_n = cnts;
            break;
        }
        cnts++;
    }

    if (min_n == 0) 
    {
        cout << -1;
    } 
    else 
    {
        cout << min_n;
    }

    return 0;
}
