#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;



int main() 
{
    int n;
    cin >> n;
    vector<string> word(n);
    for (int i = 0; i < n; i++) 
    {
        cin >> word[i];
    }

    // Please write your code here.
    sort(word.begin(), word.end());

    for(string w: word)
    {
        cout << w << endl;
    }
    return 0;
}