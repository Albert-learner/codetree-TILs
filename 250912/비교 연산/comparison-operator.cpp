#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A, B;
    cin >> A >> B;

    if(A >= B)
        cout << 1 << endl;
    else
        cout << 0 << endl;
    
    if(A > B)
        cout << 1 << endl;
    else
        cout << 0 << endl;

    if(B >= A)
        cout << 1 << endl;
    else
        cout << 0 << endl;

    if(B > A)
        cout << 1 << endl;
    else
        cout << 0 << endl;

    if(A == B)
        cout << 1 << endl;
    else
        cout << 0 << endl;

    if(A != B)
        cout << 1 << endl;
    else
        cout << 0 << endl;
    return 0;
}