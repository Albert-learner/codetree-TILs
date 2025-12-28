#include <iostream>

using namespace std;

int N;
int strange_seq(int num);

int main() 
{
    cin >> N;

    // Please write your code here.
    cout << strange_seq(N);
    return 0;
}

int strange_seq(int num)
{
    if(num == 1 || num == 2)
        return num;

    return strange_seq((int)(num / 3)) + strange_seq(num - 1);
}