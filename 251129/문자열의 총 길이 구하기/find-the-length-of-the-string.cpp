#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    int total_lengths = 0;
    vector<string> words(10);

    for(int i = 0; i < 10; i++)
    {
        cin >> words[i];
        total_lengths += words[i].length();
    }
    cout << total_lengths;
    return 0;
}