#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main() 
{
    // Please write your code here.
    string first, second, third;
    cin >> first;
    cin >> second;
    cin >> third;

    int len1 = first.length();
    int len2 = second.length();
    int len3 = third.length();
    int max_three = max({len1, len2, len3});
    int min_three = min({len1, len2, len3});

    cout << max_three - min_three;
    return 0;
}