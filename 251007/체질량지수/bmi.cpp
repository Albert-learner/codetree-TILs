#include <iostream>
#include <cmath>
using namespace std;

int main() 
{
    // Please write your code here.
    int h, w, b;
    cin >> h >> w;

    b = (10000 * w) / int(pow(h, 2));
    if(b > 25)
    {
        cout << b << endl;
        cout << "Obesity";
    }
    else
        cout << b;
    return 0;
}