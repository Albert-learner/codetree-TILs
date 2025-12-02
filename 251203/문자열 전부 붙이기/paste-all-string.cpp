#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    int N;
    cin >> N;
    vector<string> words(N);

    for(int i = 0; i < N; i++)
        cin >> words[i];

    for(int i = 0; i < N; i++)
        cout << words[i];
    return 0;
}