#include <iostream>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    int score;
    string result;
    cin >> score;

    result = (score == 100) ? "pass" : "failure";
    cout << result;
    return 0;
}