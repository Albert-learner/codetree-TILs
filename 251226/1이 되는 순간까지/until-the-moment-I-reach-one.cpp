#include <iostream>

using namespace std;

int N;
int recur_eval_sum(int num);

int main() 
{
    cin >> N;

    // Please write your code here.
    cout << recur_eval_sum(N);
    return 0;
}

int recur_eval_sum(int num)
{
    if(num == 1)
        return 0;

    if(num % 2 == 0)
        return recur_eval_sum((int)(num / 2)) + 1;
    else
        return recur_eval_sum((int)(num / 3)) + 1;
}