#include <iostream>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    string input_str;
    getline(cin, input_str);

    if(input_str.find("ee") != string::npos)
        cout << "Yes ";
    else
        cout << "No ";

    if(input_str.find("ab") != string::npos)
        cout << "Yes";
    else
        cout << "No";

    return 0;
}