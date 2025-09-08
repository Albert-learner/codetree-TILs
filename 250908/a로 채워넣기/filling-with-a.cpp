#include <iostream>
#include <string>
using namespace std;

int main() {
    // Please write your code here.

    string input_str;
    cin >> input_str;

    input_str[1] = 'a';
    input_str[input_str.length() - 2] = 'a';

    cout << input_str;    
    return 0;
}