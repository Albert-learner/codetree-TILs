#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int N;
    cin >> N;
    for(int i = 1; i <= N; i++)
    {
        if(i % 2 == 1)
        {
            for(int j = 1; j <= N; j++)
                cout << j;
        }
        else
        {
            for(int j = N; j >= 1; j--)
            {
                cout << j;
            }
        }
        cout << endl;
    }
    return 0;
}