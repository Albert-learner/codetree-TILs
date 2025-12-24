#include <iostream>

using namespace std;

int N;
void print_str(int num);

int main() 
{
    cin >> N;

    // Please write your code here.
    print_str(N);
    return 0;
}

void print_str(int num)
{
    if(num == 0)
        return;

    print_str(num - 1);
    cout << "HelloWorld\n";
}