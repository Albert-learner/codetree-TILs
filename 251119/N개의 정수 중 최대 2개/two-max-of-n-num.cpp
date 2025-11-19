#include <iostream>
#include <algorithm>
using namespace std;

int N;
int A[100];

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) 
    {
        cin >> A[i];
    }

    // Please write your code here.
    sort(A, A + N);
    reverse(A, A + N);
    cout << A[0] << ' ' << A[1];
    return 0;
}
