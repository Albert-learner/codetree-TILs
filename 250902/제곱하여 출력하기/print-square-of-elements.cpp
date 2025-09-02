#include <iostream>
#include <vector>
using namespace std;

int main() {
    // Please write your code here.

    int n, x;
    vector<int>arr;

    cin >> n;
    for(int i = 0; i < n; i++)
    {
        cin >> x;
        arr.push_back(x);
    }

    for(int i = 0; i < n; i++)
    {
        cout << arr[i] * arr[i] << ' ';
    }
    return 0;
}