#include <iostream>
using namespace std;

int main() {
    // Please write your code here.

    int N, friends = 0;
    cin >> N;


    for(int i = 1; i <= N; i++)
    {
        if(i % 2 != 0 and i % 3 != 0 and i % 5 != 0)
        {
            friends += 1;
        }
    }

    cout << friends;
    return 0;
}