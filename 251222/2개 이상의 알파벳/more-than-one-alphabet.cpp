#include <iostream>
#include <string>
#include <set>
using namespace std;

string A;

int main() 
{
    cin >> A;
    // Please write your code here.
    set<char> a_set;
    for(char c: A)
    {
        a_set.insert(c);
    }

    if(a_set.size() < 2)
        cout << "No";
    else
        cout << "Yes";

    return 0;
}