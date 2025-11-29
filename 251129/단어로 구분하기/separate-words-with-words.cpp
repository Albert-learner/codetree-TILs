#include <bits/stdc++.h>
using namespace std;

int main() 
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string line;
    getline(cin, line);     

    stringstream ss(line);
    string word;
    while (ss >> word) 
    {    
        cout << word << "\n";
    }

    return 0;
}
