#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int n;
    cin >> n;

    for(int i = 1; i < n + 1; i++)
    {
        for(int j = 1; j < n + 1; j++)
        {
            if((i + j) % 4 == 0)
                cout << "(" << i << ", " << j << ")" << endl;
            else
                cout << "(" << i << ", " << j << ")" << ' ';
        }
    }
    return 0;
}