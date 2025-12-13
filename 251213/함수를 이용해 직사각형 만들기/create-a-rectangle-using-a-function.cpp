#include <iostream>
#include <string>
using namespace std;

int n, m;
void print_str(int N, int M);

int main() {
    cin >> n >> m;

    // Please write your code here.
    print_str(n, m);
    return 0;
}

void print_str(int N, int M)
{
    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < M; j++)
        {
            cout << "1";
        }
        cout << endl;
    }
}