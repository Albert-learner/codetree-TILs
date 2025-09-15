#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int N, a, b, even_sum = 0;
    cin >> N;

    for(int i = 0; i < N; i++)
    {
        cin >> a >> b;
        for(int j = a; j <= b; j++)
        {
            if(j % 2 == 0)
                even_sum += j;
        }
        cout << even_sum << endl;
        even_sum = 0;
    }
    return 0;
}