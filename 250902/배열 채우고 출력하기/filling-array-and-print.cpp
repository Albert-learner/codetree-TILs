#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    // Please write your code here.

    char words[10];
    char chr;
    for (int i = 0; i < 10; i++)
    {
        cin >> chr;
        words[i] = chr;
    }

    reverse(begin(words), end(words));
    for(int i = 0; i < 10; i++)
    {
        cout << words[i];
    }

    return 0;
}