#include <iostream>
using namespace std;

int main() 
{
    // Please write your code here.
    int m_s, l_s, money = 0;
    cin >> m_s >> l_s;

    if(m_s >= 90)
    {
        if(l_s >= 95)
            money += 100000;
        else if(l_s >= 90)
            money += 50000;

    }
    cout << money;
    
    return 0;
}