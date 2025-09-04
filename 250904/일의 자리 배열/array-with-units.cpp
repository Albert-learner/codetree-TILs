#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int first, second, two_sum;

    cin >> first >> second;
    cout << first << ' ' << second << ' ';
    for(int i = 0; i < 8; i++)
    {
        two_sum = (first + second) % 10;
        cout << two_sum << ' ';
        first = second;
        second = two_sum;
    }
    return 0;
}