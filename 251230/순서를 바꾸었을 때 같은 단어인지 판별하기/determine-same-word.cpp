#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() 
{
    string first, second;
    cin >> first;
    cin >> second;

    sort(first.begin(), first.end());
    sort(second.begin(), second.end());

    if (first == second)
        cout << "Yes";
    else
        cout << "No";

    return 0;
}
