#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    for(int i = 1; i < 20; i++)
    {
        for(int j = 1; j < 20; j++)
        {
            if(j % 2 == 0 or j == 19)
                cout << i << " * " << j << " = " << i * j << endl;
            else
                cout << i << " * " << j << " = " << i * j << " / ";
        }
    }
    return 0;
}