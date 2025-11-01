#include <iostream>
#include <string>
using namespace std;

int main() 
{
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) 
    {
        string stars_left(n - i, '*');  
        string spaces(2 * i, ' ');      
        string stars_right(n - i, '*'); 

        cout << stars_left << spaces << stars_right << endl;
    }

    return 0;
}
