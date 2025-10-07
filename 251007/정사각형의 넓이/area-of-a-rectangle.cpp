#include <iostream>
#include <cmath>
using namespace std;

int main() 
{
    // Please write your code here.
    int N;
    cin >> N;

    if(N < 5)
    {
        cout << int(pow(N, 2)) << endl;
        cout << "tiny";
    }
    else
    {
        cout << int(pow(N, 2));
    }
    return 0;
}