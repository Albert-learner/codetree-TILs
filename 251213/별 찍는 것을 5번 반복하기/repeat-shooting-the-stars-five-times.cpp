#include <iostream>
using namespace std;

void print_stars();

int main() 
{
    // Please write your code here.
    print_stars();
    return 0;
}

void print_stars()
{
    for(int i = 0; i < 5; i++)
    {
        cout << "**********" << endl;
    }
}