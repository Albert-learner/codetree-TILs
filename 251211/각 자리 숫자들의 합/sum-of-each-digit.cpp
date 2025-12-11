#include <iostream>
#include <string>
using namespace std;

int main() 
{
    int N;
    cin >> N;

    string s = to_string(N);
    int total = 0;

    for(char c : s) 
    {
        total += c - '0';
    }

    cout << total;
    return 0;
}
