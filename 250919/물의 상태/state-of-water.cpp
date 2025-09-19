#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;

    if(N < 0)
        cout << "ice";
    else if(0 <= N < 100)
        cout << "water";
    else
        cout << "vapor";
    return 0;
}