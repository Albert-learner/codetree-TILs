#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int A, B, even_sum = 0;
    cin >> A >> B;

    for(int i = A; i <= B; i++)
    {
        if(i % 2 == 0)
            even_sum += i;
    }

    cout << even_sum;
    return 0;
}