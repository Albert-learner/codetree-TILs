#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    char inp_chr;
    int row, height;
    cin >> row >> height >> inp_chr;

    while(inp_chr != 'C')
    {
        cout << row * height << endl;
        cin >> row >> height >> inp_chr;
    }
    cout << row * height;
    return 0;
}