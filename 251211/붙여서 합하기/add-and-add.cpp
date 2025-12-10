#include <iostream>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    string first, second;
    int s_first = 0, s_second = 0;
    cin >> first >> second;

    s_first = stoi(first + second);
    s_second = stoi(second + first);

    cout << s_first + s_second;
    return 0;
}