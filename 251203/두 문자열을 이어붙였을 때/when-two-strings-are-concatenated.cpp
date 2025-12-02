#include <iostream>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    string first, second, front, end;
    getline(cin, first);
    getline(cin, second);
    cin.ignore();

    front = first + second;
    end = second + first;

    if(front == end)
        cout << "true";
    else
        cout << "false";
    return 0;
}