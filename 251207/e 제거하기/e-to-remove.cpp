#include <iostream>
#include <string>
using namespace std;

int main() 
{
    string input_str;
    cin >> input_str;

    size_t first_idx = input_str.find('e');

    if (first_idx != string::npos) 
    {
        input_str.erase(first_idx, 1);  
    }

    cout << input_str;

    return 0;
}
