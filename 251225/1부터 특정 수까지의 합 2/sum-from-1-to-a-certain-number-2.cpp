#include <iostream>

using namespace std;

int N;
int recur_sum(int num);

int main() 
{
    cin >> N;

    // Please write your code here.
    cout << recur_sum(N);
    return 0;
}

int recur_sum(int num)
{
    if(num == 1)
        return 1;

    return recur_sum(num - 1) + num;
}