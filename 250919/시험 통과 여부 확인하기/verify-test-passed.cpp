#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N, diff = 0;
    cin >> N;

    if(N >= 80)
        cout << "pass";
    else
    {
        diff = 80 - N;
        cout << diff << " more score";
    }
    return 0;
}