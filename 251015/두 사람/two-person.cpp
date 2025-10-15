#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int f_a, s_a;
    char f_g, s_g;
    cin >> f_a >> f_g;
    cin >> s_a >> s_g;

    if((f_a >= 19 && f_g == 'M') || (s_a >= 19 && s_g == 'M'))
        cout << 1;
    else
        cout << 0;
        
    return 0;
}