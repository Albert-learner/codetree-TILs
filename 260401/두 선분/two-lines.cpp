#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int x1, x2, x3, x4, tmp, tmp_;
    cin >> x1 >> x2 >> x3 >> x4;

    if(x2 > x4)
    {
        tmp = x1;
        x1 = x3;
        x3 = x1;

        tmp_ = x2;
        x2 = x4;
        x4 = tmp_;
    }

    if(x2 >= x3)
        cout << "intersecting";
    else
        cout << "nonintersecting";
    return 0;
}