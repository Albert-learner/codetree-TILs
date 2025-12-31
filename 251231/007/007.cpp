#include <iostream>
#include <string>
using namespace std;

class INFO
{
    public:
        string sc_code;
        char met_pnt;
        int tm;
        void print_info();
};

int main() 
{
    string secret_code;
    char meeting_point;
    int time;
    cin >> secret_code >> meeting_point >> time;

    // Please write your code here.
    INFO info;
    info.sc_code = secret_code;
    info.met_pnt = meeting_point;
    info.tm = time;

    info.print_info();
    return 0;
}

void INFO::print_info()
{
    cout << "secret code : " << sc_code << endl;
    cout << "meeting point : " << met_pnt << endl;
    cout << "time : " << tm;
}