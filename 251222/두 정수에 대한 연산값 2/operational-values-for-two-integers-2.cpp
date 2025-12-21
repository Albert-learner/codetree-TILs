#include <iostream>

using namespace std;

int a, b;
pair<int, int> operate(int a, int b);

int main() 
{
    cin >> a >> b;
    
    // Please write your code here.
    auto result = operate(a, b);
    cout << result.first << ' ' << result.second;
    return 0;
}

pair<int, int> operate(int a, int b)
{
    if(a < b)
    {
        a += 10;
        b *= 2;
    }
    else
    {
        b += 10;
        a *= 2;
    }

    return {a, b};
}