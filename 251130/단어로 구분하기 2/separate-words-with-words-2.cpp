#include <iostream>
#include <sstream>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    string line;
    getline(cin, line);

    stringstream ss(line);
    string word;
    int idx = 1;

    while(ss >> word)
    {
        if(idx % 2 == 1)
            cout << word << endl;
        
        idx += 1;
    }
    return 0;
}