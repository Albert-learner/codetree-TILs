#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int arr[4][4], fives = 0;

    for(int i = 0; i < 4; i++)
    {
        for(int j = 0; j < 4; j++)
        {
            cin >> arr[i][j];
            if(arr[i][j] % 5 == 0)
                fives += 1;
        }
    }
    cout << fives;
    return 0;
}