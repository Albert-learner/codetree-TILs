#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    char inp_chr, prev_chr;
    cin >> inp_chr;

    if(inp_chr != 'a')
    {
        prev_chr = (char)((int)inp_chr - 1);
    }
    else
    {
        prev_chr = 'z';
    }
    cout << prev_chr;
    return 0;
}