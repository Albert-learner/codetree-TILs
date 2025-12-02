#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() 
{
    // Please write your code here.
    int N;
    string line, nums_str, temp;
    cin >> N;
    cin.ignore();
    getline(cin, line);

    stringstream ss(line);
    while(ss >> temp)
        nums_str += temp;

    for(int i = 0; i < nums_str.length(); i++)
    {
        if((i + 1) % 5 == 0)
            cout << nums_str[i] << endl;
        else
            cout << nums_str[i];
    }
    return 0;
}