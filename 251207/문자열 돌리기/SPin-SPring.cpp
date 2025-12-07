#include <iostream>
#include <string>
using namespace std;

int main() 
{
    string input_str;
    cin >> input_str;

    int s_len = input_str.length();

    for (int i = 0; i <= s_len; i++) 
    {

        string part1 = (i == 0 ? "" : input_str.substr(s_len - i, i));
        string part2 = input_str.substr(0, s_len - i);

        cout << part1 + part2 << "\n";
    }

    return 0;
}
