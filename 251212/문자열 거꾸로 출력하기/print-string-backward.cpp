#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() 
{
    string input_str;

    while (true) 
    {
        getline(cin, input_str);

        if (input_str == "END")
            break;

        reverse(input_str.begin(), input_str.end());
        cout << input_str << endl;
    }

    return 0;
}
