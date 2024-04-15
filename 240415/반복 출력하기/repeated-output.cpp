#include <iostream>
using namespace std;

void print_n_lines(int n)
{
    for (int i = 0; i < n; i++)
        cout << "12345^&*()_" << endl;
}

int main() {
    
    int N;
    cin >> N;

    print_n_lines(N);
    return 0;
}