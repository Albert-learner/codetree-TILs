#include <iostream>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    string first, second;
    cin >> first >> second;

    if(second.size() >= 2 && first.size() >= 2)
    {
        second[0] = first[0];
        second[1] = first[1];
    }

    cout << second;
    return 0;
}