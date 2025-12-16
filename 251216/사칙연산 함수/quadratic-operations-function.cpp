#include <iostream>
#include <string>
using namespace std;

int a;
int c;
string o;

int add(int a, int b);
int diff(int a, int b);
int multiply(int a, int b);
int divide(int a, int b);

int main() 
{
    cin >> a >> o >> c;

    // Please write your code here.
    if (o == "+" || o == "-" || o == "*" || o == "/") 
    {
        if (o == "+") 
        {
            cout << a << " " << o << " " << c << " = " << add(a, c);
        } 
        else if (o == "-") 
        {
            cout << a << " " << o << " " << c << " = " << diff(a, c);
        } 
        else if (o == "*") 
        {
            cout << a << " " << o << " " << c << " = " << multiply(a, c);
        } 
        else 
        { // "/"
            cout << a << " " << o << " " << c << " = " << divide(a, c);
        }
    } 
    else 
    {
        cout << "false";
    }

    return 0;
}

int add(int a, int b)
{
    return a + b;
}

int diff(int a, int b)
{
    return a - b;
}

int multiply(int a, int b)
{
    return a * b;
}

int divide(int a, int b)
{
    return a / b;
}
