#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

int main() 
{
    // Please write your code here.
    string line, word;
    getline(cin, line);
    vector<string> words;

    stringstream ss(line);
    while(ss >> word)
        words.push_back(word);

    for (int i = words.size() - 1; i >= 0; i--) 
    {
        cout << words[i] << "\n";
    }    
    return 0;
}