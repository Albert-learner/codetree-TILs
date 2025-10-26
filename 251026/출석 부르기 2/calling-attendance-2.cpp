#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() 
{
    // Please write your code here.
    int n;
    map<int, string> students = {
        {1, "John"}, 
        {2, "Tom"}, 
        {3, "Paul"}, 
        {4, "Sam"}
    };
    cin >> n;

    while(n >= 1 && n <= 4)
    {
        cout << students[n] << endl;
        cin >> n;
    }
    cout << "Vacancy";
    return 0;
}