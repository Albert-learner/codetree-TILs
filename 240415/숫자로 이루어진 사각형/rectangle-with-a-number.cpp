#include <iostream>
#include <cmath>
using namespace std;

void print_rect_numbers(int n)
{
    for (int i = 1; i <= int(pow(n, 2)); i++)
    {
        if (i % 4 == 0)
        {
            if (i > 10)
                cout << i - 9 << endl;
            else
                cout << i << endl;
        }
        else
        {
            if (i < 10)
            {
                cout << i << ' ';
            }
            else
            {
                cout << i - 9 << ' ';
            }
        }
    }
}

int main() {
    int N;
    cin >> N;

    print_rect_numbers(N);
    return 0;
}