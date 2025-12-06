#include <iostream>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    string word, result = "";
    getline(cin, word);

    int len = word.length();
    for(int i = 0; i < len; i++)
    {
        if(i != 1 && i != len - 2)
            result += word[i];
    }

    cout << result;
    return 0;
}