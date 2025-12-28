#include <iostream>

using namespace std;

int N;
int recur_seq(int num);

int main() 
{
    cin >> N;

    // Please write your code here.
    cout << recur_seq(N);
    return 0;
}

int recur_seq(int num)
{
    if(num == 1)
        return 2;
    else if(num == 2)
        return 4;

    return recur_seq(num - 2) * recur_seq(num - 1) % 100;
}