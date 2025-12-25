#include <iostream>

using namespace std;

int n;
void print_star(int num);

int main() 
{
    cin >> n;

    // Please write your code here.
    print_star(n);
    return 0;
}

void print_star(int num)
{
    if(num == 0)
        return ;

    for(int i = 0; i < num; i++)
        cout << '*';
    print_star(num - 1);
    for(int i = 0; i < num; i++)
        cout << '*';
}