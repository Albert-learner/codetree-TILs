#include <iostream>
using namespace std;

void print_5_10_stars()
{
    for (int i = 0; i < 5; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            cout << "*";
        }
        cout << endl;
    }
}

int main() {
    print_5_10_stars();
    return 0;
}