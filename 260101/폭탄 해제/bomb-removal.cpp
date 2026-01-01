#include <iostream>
#include <string>

using namespace std;

class CODE 
{
    public:
        string code;
        string color;
        int second;

        CODE(string c, string col, int s)
            : code(c), color(col), second(s) {}

        void print_code() {
            cout << "code : " << code << endl;
            cout << "color : " << color << endl;
            cout << "second : " << second << endl;
        }
};

int main() 
{
    string code, color;
    int second;

    cin >> code >> color >> second;

    CODE code_inst(code, color, second);
    code_inst.print_code();

    return 0;
}
