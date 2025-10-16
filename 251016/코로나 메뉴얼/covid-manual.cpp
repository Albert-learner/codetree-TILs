#include <iostream>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    string stat1, stat2, stat3;
    int deg1, deg2, deg3, emergency = 0;
    
    cin >> stat1 >> deg1;
    cin >> stat2 >> deg2;
    cin >> stat3 >> deg3;

    if(stat1 == "Y" && deg1 >= 37)
        emergency += 1;
    if(stat2 == "Y" && deg2 >= 37)
        emergency += 1;
    if(stat3 == "Y" && deg3 >= 37)
        emergency += 1;

    if(emergency >= 2)
        cout << 'E';
    else
        cout << 'N';

    return 0;
}