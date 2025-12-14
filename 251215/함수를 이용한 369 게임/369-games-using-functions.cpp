#include <iostream>
#include <string>
using namespace std;

int a, b;
int count_threes(int A, int B);

int main() 
{
    cin >> a >> b;

    // Please write your code here.
    cout << count_threes(a, b);
    return 0;
}

int count_threes(int a, int b)
{
    int three_cnts = 0;
    for(int i = a; i < b + 1; i++)
    {
        string i_str = to_string(i);
        if(i % 3 == 0 || i_str.find('3') != string::npos || i_str.find('6') != string::npos || i_str.find('9') != string::npos)
            three_cnts += 1;
    }

    return three_cnts;
}