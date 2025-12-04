#include <iostream>
#include <string>
using namespace std;

int main() 
{
    string input_str;
    cin >> input_str;  

    int firsts = 0, seconds = 0;

    for (int i = 0; i < input_str.length() - 1; i++) 
    {
        if (input_str.substr(i, 2) == "ee") 
        {
            firsts++;
        }
        else if (input_str.substr(i, 2) == "eb") 
        {
            seconds++;
        }
    }

    cout << firsts << " " << seconds;

    return 0;
}
