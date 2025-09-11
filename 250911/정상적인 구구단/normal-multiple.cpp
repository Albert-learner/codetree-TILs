#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N;
    cin >> N;

    for(int i = 1; i <= N; i++)
    {
        for(int j = 1; j <= N; j++)
        {
            if(j != N)
                cout << i << " * " << j << " = " << i * j << ", ";
            else
                cout << i << " * " << j << " = " << i * j;
        }
        cout << endl;
    }
    return 0;
}