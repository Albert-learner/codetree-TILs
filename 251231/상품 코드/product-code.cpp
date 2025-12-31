#include <iostream>
#include <string>

using namespace std;

class PRODUCT {
public:
    string prod;
    string code;

    // 기본 생성자 (디폴트 값)
    PRODUCT(string p = "codetree", string c = "50")
        : prod(p), code(c) {}

    void print_info() {
        cout << "product " << code << " is " << prod << endl;
    }
};

int main() {
    string product, code;
    cin >> product >> code;

    // 기본 객체
    PRODUCT product_inst;
    product_inst.print_info();

    // 입력값으로 생성한 객체
    product_inst = PRODUCT(product, code);
    product_inst.print_info();

    return 0;
}
