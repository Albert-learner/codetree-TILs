#include <iostream>
#include <iomanip>
using namespace std;

int main() 
{
    // Please write your code here.
    float feet = 30.48;
    float N;
    cin >> N;

    cout << fixed << setprecision(1) << feet * N;
    return 0;
}