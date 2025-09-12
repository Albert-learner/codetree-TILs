#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A, B;
    cin >> A >> B;

    cout << fixed;
    cout.precision(1);
    cout << A + B << ' ' << (A + B) / 2.0;
    return 0;
}