#include <iostream>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    string input_str;
    char find_chr;
    int find_cnts = 0;

    getline(cin, input_str);
    cin >> find_chr;

    for(int i = 0; i < input_str.length(); i++)
    {
        if(input_str[i] == find_chr)
            find_cnts += 1;
    }
    cout << find_cnts;
    return 0;
}