#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    char inp_chr;
    cin >> inp_chr;

    if(inp_chr != 'z')
        cout << char((int)inp_chr + 1);
    else
    {
        cout << 'a';
    }
    return 0;
}