#include <iostream>

using namespace std;

int N;
void print_number(int num);

int main() 
{
    cin >> N;

    // Please write your code here.
    print_number(N);
    return 0;
}

void print_number(int num)
{
    if(num == 0)
        return ;

    cout << num << ' ';
    print_number(num - 1);
    cout << num << ' ';
}