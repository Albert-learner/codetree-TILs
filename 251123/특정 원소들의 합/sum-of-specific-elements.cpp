#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int arr[4][4], area_sum = 0;

    for(int i = 0; i < 4; i++)
    {
        for(int j = 0; j < 4; j++)
        {
            cin >> arr[i][j];
            if(i >= j)
                area_sum += arr[i][j];
        }
    }
    cout << area_sum;
    return 0;
}
