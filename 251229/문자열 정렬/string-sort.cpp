#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() 
{
    string input_str;
    cin >> input_str;

    sort(input_str.begin(), input_str.end());

    cout << input_str;
    return 0;
}
