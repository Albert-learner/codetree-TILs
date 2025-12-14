#include <iostream>
using namespace std;

int print_rectangle(int num)
{
    int num_sum = 0;
    for (int i = 1; i <= num; ++i)
    {
        num_sum += i;
    }

    return num_sum / 10;
}

int main() {
    int N;
    cin >> N;

    cout << print_rectangle(N);
    return 0;
}
