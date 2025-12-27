#include <iostream>

using namespace std;

int n;
int recur_seq(int num);

int main() 
{
    cin >> n;

    // Please write your code here.
    cout << recur_seq(n);
    return 0;
}

int recur_seq(int num)
{
    if(num == 1)
        return 0;

    if(num % 2 == 0)
        return recur_seq((int)(num / 2)) + 1;
    else
        return recur_seq((int)(num / 3 + 1)) + 1;
}