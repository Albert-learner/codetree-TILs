#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    int n, same_cnts = 0;
    string a_str;
    cin >> n >> a_str;
    vector<string> words(n);

    for(int i = 0; i < n; i++)
    {
        cin >> words[i];
    }

    for(string word: words)
    {
        if(word == a_str)
            same_cnts += 1;
    }
    cout << same_cnts;
    return 0;
}