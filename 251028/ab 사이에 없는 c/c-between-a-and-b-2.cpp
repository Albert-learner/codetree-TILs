#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int a, b, c, c_nums = 0;
    cin >> a >> b >> c;

    for(int i = a; i <= b; i++)
    {
        if(i % c == 0)
        {
            c_nums += 1;
        }
    }

    if(c_nums == 0)
        cout << "YES";
    else
        cout << "NO";
        
    return 0;
}