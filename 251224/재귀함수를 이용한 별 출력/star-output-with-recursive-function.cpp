#include <iostream>

using namespace std;


void print_star(int num);

int main() 
{
    int n;
    cin >> n;

    // Please write your code here.
    print_star(n);
    return 0;
}

void print_star(int num)
{
    if(num == 0)
        return ;

    print_star(num - 1);
    for(int i = 0; i < num; i++)
        cout << '*';
    cout << endl;
}