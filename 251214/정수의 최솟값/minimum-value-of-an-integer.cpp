#include <iostream>
using namespace std;

int compare(int a, int b, int c);

int main() 
{
    int x, y, z;
    cin >> x >> y >> z;

    cout << compare(x, y, z);
    return 0;
}

int compare(int a, int b, int c)
{
    return min(a, min(b, c));
}