#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int N;
    cin >> N;

    if(N >= 3000)
        cout << "book";
    else if(1000 <= N and N < 3000)
        cout << "mask";
    else
        cout << "no";
    return 0;
}