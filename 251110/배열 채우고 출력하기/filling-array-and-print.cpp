#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() 
{
    // Please write your code here.
    vector<char> words(10);
    for(int i = 0; i < 10; i++)
    {
        cin >> words[i];
    }

    reverse(words.begin(), words.end());
    for(int i = 0; i < 10; i++)
    {
        cout << words[i];
    }
    return 0;
}