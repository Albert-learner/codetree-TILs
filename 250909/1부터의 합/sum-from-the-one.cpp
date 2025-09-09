#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N, i_sum = 0, i_num;
    cin >> N;

    for(int i = 1; i <= 100; i++)
    {
        i_sum += i;

        if(i_sum >= N)
        {
            i_num = i;
            break;
        }
    }

    cout << i_num;
    return 0;
}