#include <iostream>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    string S, T, tmp;
    cin >> S;
    cin >> T;

    tmp = S;
    S = T;
    T = tmp;

    cout << S << endl;
    cout << T << endl;
    return 0;
}