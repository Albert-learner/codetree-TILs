#include <iostream>
#include <string>

using namespace std;

class PRODUCT 
{
public:
    string prod;
    string code;

    PRODUCT(string p = "codetree", string c = "50")
        : prod(p), code(c) {}

    void print_info() 
    {
        cout << "product " << code << " is " << prod << endl;
    }
};

int main() 
{
    string product, code;
    cin >> product >> code;

    PRODUCT product_inst;
    product_inst.print_info();

    product_inst = PRODUCT(product, code);
    product_inst.print_info();

    return 0;
}
