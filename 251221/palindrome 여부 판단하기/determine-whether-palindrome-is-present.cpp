#include <iostream>
#include <string>
using namespace std;

string A;
string is_palindrome(const string& a_str);

int main() 
{
    cin >> A;

    // Please write your code here.
    cout << is_palindrome(A);
    return 0;
}

string is_palindrome(const string& a_str)
{
    string rev = string(a_str.rbegin(), a_str.rend());
    if(a_str == rev)
        return "Yes";
    else
        return "No";
}