#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() 
{
    string input_str;
    getline(cin, input_str);   

    int N;
    cin >> N;

    reverse(input_str.begin(), input_str.end());

    for (int i = 0; i < N && i < input_str.length(); i++) 
    {
        cout << input_str[i];
    }

    return 0;
}
