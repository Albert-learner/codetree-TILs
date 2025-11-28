#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() 
{
    // Please write your code here.
    vector<string> words(4);

    for(int i = 0; i < 4; i++)
    {
        cin >> words[i];
    }
    reverse(words.begin(), words.end());

    for(string word: words)
    {
        cout << word << endl;
    }
    return 0;
}