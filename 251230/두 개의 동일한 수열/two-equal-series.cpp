#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() 
{
    int n;
    cin >> n;
    vector<int> A(n);
    vector<int> B(n);

    for (int i = 0; i < n; i++) 
    {
        cin >> A[i];
    }

    for (int i = 0; i < n; i++) 
    {
        cin >> B[i];
    }

    // Please write your code here.
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());

    if(A == B)
        cout << "Yes";
    else
        cout << "No";

    return 0;
}