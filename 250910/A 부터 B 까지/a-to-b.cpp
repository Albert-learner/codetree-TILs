#include <iostream>
using namespace std;

int main() {
    // Please write your code here.

    int A, B;
    cin >> A >> B;

    cout << A << ' ';
    while(A <= B)
    {
        if(A % 2 == 0)
            A += 3;
        else
            A *= 2;

        if(A > B)
            break;

        cout << A << ' ';
    }
    return 0;
}